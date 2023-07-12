from io import BytesIO
from pydantic import BaseModel
from main import document_manager
from bimo_core import logging, DocumentMetadata
from fastapi import APIRouter, BackgroundTasks, Body, File, Form, UploadFile
from controllers import document_controller
from datetime import datetime
import uuid

router = APIRouter(prefix="/documents")

class UploadFileRequestArgs(BaseModel):
    user_id: str
    section_id: str
    assignment_id: str = None

@router.post("/upload")
async def upload_file(
    background_tasks: BackgroundTasks, 
    file: UploadFile = File(...), 
    user_id: str = Form(...), 
    section_id: str = Form(None), 
    assignment_id: str = Form(None)
):
    document_id = str(uuid.uuid4())
    logging.info(f"Uploading file {file.filename} for user {user_id}")
    file_content = await file.read()
    file_stream = BytesIO(file_content)
    metadata = DocumentMetadata(
        id=document_id,
        user_id=user_id,
        name=file.filename,
    )

    try:
        # Upload the document to GCS and return the signed url to the client
        signed_url = document_manager.upload_document(metadata, file_stream)
    except Exception as e:
        logging.error(f"Failed to upload file {file.filename} for user {user_id}")
        logging.error(e)
        return {"error": "Failed to upload file"}
    
    try:
        # Reset the pointer to the beginning of the file stream
        file_stream.seek(0)
        # Upload the embeddings to the vector store in the background
        background_tasks.add_task(document_manager.upload_embeddings, metadata, file_stream)
    except Exception as e:
        logging.error(f"Failed to upload embeddings for file {file.filename} for user {user_id}")
        logging.error(e)
        return {"error": "Failed to upload embeddings"}
    
    document = document_controller.add_document(
        id=document_id, 
        name=file.filename, 
        type=file.content_type, 
        url=signed_url, 
        section_id=section_id, 
        assignment_id=assignment_id, 
        user_id=user_id
    )
    
    logging.info(f"Uploaded document {file.filename} for user {user_id}")

    return {
        "id": document.id,
        "name": document.name,
        "type": document.type,
        "url": document.url,
        "course_id": document.section_id,
        "assignment_id": document.assignment_id,
        "user_id": document.user_id
    }
