import uuid
from io import BytesIO
from fastapi import APIRouter, UploadFile
from main import mongo, document_manager
from momoai_core import MongoCollections, DocumentMetadata, logging


router = APIRouter(prefix="/users")

@router.get("/")
def getUsers():
    return {"message": "users"}

@router.get("/add/{_id}/{first_name}/{last_name}")
def addUser(_id: str, first_name: str, last_name: str):
    mongo.insert(data={"_id": _id, "first_name": first_name, "last_name": last_name}, collection=MongoCollections.users)

@router.post("/upload")
async def upload_file(file: UploadFile, user_id: str, document_id: str):
    file_content = await file.read()
    file_content = BytesIO(file_content)
    metadata = DocumentMetadata()
    metadata.id = document_id
    metadata.user_id = user_id
    document_manager.upload_document(metadata, file_content)
