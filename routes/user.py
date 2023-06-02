import uuid
from io import BytesIO
from fastapi import APIRouter, File, Form, UploadFile, Body
from main import mongo, document_manager
from momoai_core import MongoCollections, DocumentMetadata, logging
from pydantic import BaseModel


router = APIRouter(prefix="/user")

@router.get("/")
def getUsers():
    return {"message": "users"}

@router.get("/add/{_id}/{first_name}/{last_name}")
def addUser(_id: str, first_name: str, last_name: str):
    mongo.insert(data={"_id": _id, "first_name": first_name, "last_name": last_name}, collection=MongoCollections.users)

class UploadFileRequestArgs(BaseModel):
    user_id: str
    document_id: str

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), user_id: str = Form(...), document_id: str = Form(...)):
    logging.info(f"Uploading file {file.filename} for user {user_id}")
    file_content = await file.read()
    print(user_id)
    file_content = BytesIO(file_content)
    metadata = DocumentMetadata(
        id=document_id,
        user_id=user_id,
        name=file.filename,
    )
    document_manager.upload_document(metadata, file_content)
    logging.info(f"Uploaded file {file.filename} for user {user_id}")
