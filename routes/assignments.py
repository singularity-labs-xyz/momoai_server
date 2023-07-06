import uuid

from pydantic import BaseModel
from fastapi import APIRouter
from momoai_core import logging
from controllers import assignment_controller
from datetime import datetime

router = APIRouter(prefix="/assignments")

@router.get("/{assignment_id}")
def getAssignment(assignment_id: str):
    assignment = assignment_controller.get_assignment(id=assignment_id)

    return {
        "id": assignment.id,
        "name": assignment.name, 
        "date": assignment.date,
        "description": assignment.description,
        "priority": assignment.priority,
        "completed": assignment.completed,
        "course_id": assignment.course_id,
        "event_id": assignment.event_id,
        "user_id": assignment.user_id,
    }

class AddAssignmentRequestArgs(BaseModel):
    name: str
    date: datetime
    description: str
    priority: int
    course_id: str
    event_id: str
    user_id: str

@router.post("/add")
def addAssignment(body: AddAssignmentRequestArgs):
    assignment = assignment_controller.add_assignment(id=str(uuid.uuid4()), name=body.name, due_date=body.date, description=body.description, priority=body.priority, course_id=body.course_id, event_id=body.event_id, user_id=body.user_id)
    logging.info(f"Added assignment {assignment.name} with id {assignment.id}")

    return{
        "id": assignment.id,
        "name": assignment.name,
        "date": assignment.due_date,
        "description": assignment.description,
        "priority": assignment.priority,
        "completed": assignment.completed,
        "course_id": assignment.course_id,
        "user_id": assignment.user_id
    }

@router.delete("/{school_id}")
def deleteAssignment(assignment_id: str):
    assignment_controller.delete_assignment(id=assignment_id)
    logging.info(f"Deleted assignment with id {assignment_id}")
    return{"message": "Assignment deleted successfully"}