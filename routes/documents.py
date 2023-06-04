from io import BytesIO
from pydantic import BaseModel
from main import document_manager
from momoai_core import logging, DocumentMetadata
from fastapi import APIRouter, BackgroundTasks, Body, File, Form, UploadFile

router = APIRouter(prefix="/documents")

class UploadFileRequestArgs(BaseModel):
    user_id: str
    document_id: str

@router.post("/upload")
async def upload_file(background_tasks: BackgroundTasks, file: UploadFile = File(...), user_id: str = Form(...), document_id: str = Form(...)):
    logging.info(f"Uploading file {file.filename} for user {user_id}")
    file_content = await file.read()
    file_stream = BytesIO(file_content)
    metadata = DocumentMetadata(
        id=document_id,
        user_id=user_id,
        name=file.filename,
    )
    # Upload the document to GCS and return the signed url to the client
    signed_url = document_manager.upload_document(metadata, file_stream)
    # Reset the pointer to the beginning of the file stream
    file_stream.seek(0)
    # Upload the embeddings to the vector store in the background
    background_tasks.add_task(document_manager.upload_embeddings, metadata, file_stream)
    logging.info(f"Uploaded file {file.filename} for user {user_id}")
    return {"url": signed_url}
