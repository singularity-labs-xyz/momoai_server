from main import session
from database.models import Assignment

from datetime import datetime

def get_assignment(id: str):
    assignment = session.query(Assignment).filter(Assignment.id == id).first()

    return assignment

def add_assignment(id: str, name: str, due_date: datetime, description: str, priority: int, course_id: str, event_id: str, user_id: str):
    assignment = Assignment(id=id, name=name, due_date=due_date, description=description, priority=priority, completed=False, course_id=course_id, event_id=event_id, user_id=user_id)
    session.add(assignment)
    session.commit()

    return assignment

def delete_assignment(id: str):
    assignment = session.query(Assignment).filter(Assignment.id == id).first()
    session.delete(assignment)
    session.commit()

    return assignment
    