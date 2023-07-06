
from main import session
from database.models import Event
from datetime import datetime

def get_event(id: str):
    event = session.query(Event).filter(Event.id == id).first()
    return event

def add_event(id: str, name: str, start_time: datetime, description: str, end_time: datetime, priority: int, course_id: str, user_id: str):
    event = Event(id=id, name=name, start_time=start_time, description=description, end_time=end_time, priority=priority, course_id=course_id, user_id=user_id)
    session.add(event)
    session.commit()
    return event

def delete_event(id: str):
    event = session.query(Event).filter(Event.id == id).first()
    session.delete(event)
    session.commit()

    return event