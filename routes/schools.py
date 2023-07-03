import uuid

from pydantic import BaseModel
from fastapi import APIRouter
from momoai_core import logging
from controllers import school_controller

router = APIRouter(prefix="/schools")

@router.get("/{school_id}")
def getUsers(school_id: str):
    school = school_controller.get_school(id=school_id)

    return {
        "id": school.id,
        "name": school.name
    }

class AddSchoolRequestArgs(BaseModel):
    name: str

@router.post("/add")
def addSchool(body: AddSchoolRequestArgs):
    school = school_controller.add_school(id=str(uuid.uuid4()), name=body.name)
    logging.info(f"Added school {school.name} with id {school.id}")

    return{
        "id": school.id,
        "name": school.name
    }

@router.delete("/{school_id}")
def deleteSchool(school_id: str):
    school_controller.delete_school(id=school_id)
    logging.info(f"Deleted school with id {school_id}")
    return{"message": "School deleted successfully"}