from fastapi import APIRouter
from momoai_core import logging
from main import mongo_client
from momoai_core import MongoCollections

router = APIRouter(prefix="/users")

@router.get("/")
def getUsers():
    return {"message": "users"}

@router.get("/add_user/{_id}/{first_name}/{last_name}")
def addUser(_id: str, first_name: str, last_name: str):
    mongo_client.insert(data={"_id": _id, "first_name": first_name, "last_name": last_name}, collection=MongoCollections.users)



