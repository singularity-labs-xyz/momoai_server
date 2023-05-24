import uuid
from io import BytesIO
from fastapi import APIRouter, File, Form, UploadFile
from main import mongo, document_manager
from momoai_core import MongoCollections, DocumentMetadata, logging


router = APIRouter(prefix="/user")

@router.get("/")
def getUsers():
    return {"message": "users"}

@router.get("/add/{_id}/{first_name}/{last_name}")
def addUser(_id: str, first_name: str, last_name: str):
    mongo.insert(data={"_id": _id, "first_name": first_name, "last_name": last_name}, collection=MongoCollections.users)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), user_id: str = Form(...), document_id: str = Form(...)):
    logging.info(f"Uploading file {file.filename} for user {user_id}")
    file_content = await file.read()
    print(user_id)
    file_content = BytesIO(file_content)
    metadata = DocumentMetadata()
    metadata.id = document_id
    metadata.user_id = user_id
    document_manager.upload_document(metadata, file_content)
    logging.info(f"Uploaded file {file.filename} for user {user_id}")
