import uuid

from pydantic import BaseModel
from fastapi import APIRouter
from momoai_core import logging
from controllers import event_controller
from datetime import datetime

router = APIRouter(prefix="/events")

@router.get("/{event_id}")
def getEvent(event_id: str):
    event = event_controller.get_event(id=event_id)

    return {
        "id": event.id,
        "name": event.name, 
        "date": event.date,
        "description": event.description,
        "priority": event.priority,
        "completed": event.completed,
        "course_id": event.course_id,
        "user_id": event.user_id,
    }

class AddEventRequestArgs(BaseModel):
    name: str
    start_time: datetime
    end_time: datetime
    description: str
    priority: int
    course_id: str = None
    user_id: str

@router.post("/add")
def addEvent(body: AddEventRequestArgs):
    event = event_controller.add_event(id=str(uuid.uuid4()), name=body.name, start_time=body.start_time, end_time=body.end_time, description=body.description, priority=body.priority, course_id=body.course_id, user_id=body.user_id)
    logging.info(f"Added event {event.name} with id {event.id}")

    return{
        "id": event.id,
        "name": event.name,
        "start_time": event.start_time,
        "end_time": event.end_time,
        "description": event.description,
        "priority": event.priority,
        "course_id": event.course_id,
        "user_id": event.user_id
    }

@router.delete("/{event_id}")
def deleteEvent(event_id: str):
    event_controller.delete_event(id=event_id)
    logging.info(f"Deleted event with id {event_id}")
    return{"message": "Event deleted successfully"}