import uuid

from pydantic import BaseModel
from fastapi import APIRouter
from momoai_core import logging
from controllers import user_controller

router = APIRouter(prefix="/users")

@router.get("/{user_id}")
def getUser(user_id: str):
    user = user_controller.get_user(id=user_id)
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "school_id": user.school_id
    }

class AddUserRequestArgs(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    school_id: str

@router.post("/add")
def addUser(body: AddUserRequestArgs):
    user = user_controller.add_user(id=str(uuid.uuid4()), first_name=body.first_name, last_name=body.last_name, email=body.email, password=body.password, school_id=body.school_id)
    logging.info(f"Added user {user.first_name} {user.last_name} with id {user.id}")

    return{
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "school_id": user.school_id
    }

@router.delete("/{user_id}")
def deleteUser(user_id: str):
    user_controller.delete_user(id=user_id)
    logging.info(f"Deleted user with id {user_id}")
    return{"message": "User deleted successfully"}
    
