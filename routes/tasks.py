import uuid

from pydantic import BaseModel
from fastapi import APIRouter
from bimo_core import logging
from controllers import task_controller
from datetime import datetime

router = APIRouter(prefix="/tasks")

@router.get("/{task_id}")
def getTask(task_id: str):
    task = task_controller.get_task(id=task_id)
    return {
        "id": task.id,
        "name": task.name, 
        "date": task.date,
        "description": task.description,
        "priority": task.priority,
        "status": task.status,
        "assignment_id": task.assignment_id,
        "section_id": task.section_id,
        "event_id": task.event_id,
        "user_id": task.user_id,
    }

class AddTaskRequestArgs(BaseModel):
    name: str
    date: datetime
    description: str
    priority: int
    user_id: str
    assignment_id: str = None
    section_id: str = None
    event_id: str = None

@router.post("/add")
def addTask(body: AddTaskRequestArgs):
    task = task_controller.add_task(
        id=str(uuid.uuid4()), 
        name=body.name, 
        date=body.date, 
        description=body.description, 
        priority=body.priority, 
        assignment_id=body.assignment_id, 
        section_id=body.section_id, 
        event_id=body.event_id, 
        user_id=body.user_id
    )

    logging.info(f"Added task {task.name} with id {task.id}")

    return{
        "id": task.id,
        "name": task.name,
        "date": task.date,
        "description": task.description,
        "priority": task.priority,
        "status": task.status,
        "assignment_id": task.assignment_id,
        "section_id": task.section_id,
        "event_id": task.event_id,
        "user_id": task.user_id
    }

@router.delete("/{task_id}")
def deleteTask(task_id: str):
    task_controller.delete_task(id=task_id)
    logging.info(f"Deleted task with id {task_id}")
    return{"message": "Task deleted successfully"}