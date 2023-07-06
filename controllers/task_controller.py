
from main import session
from database.models import Task

def get_task(id: str):
    task = session.query(Task).filter(Task.id == id).first()
    return task

def add_task(
    id: str,
    name: str,
    date: str,
    description: str,
    priority: int,
    completed: bool,
    user_id: str,
    assignment_id: str,
    course_id: str,
    event_id: str,
):
    task = Task(
        id=id,
        name=name,
        date=date,
        description=description,
        priority=priority,
        completed=completed,
        user_id=user_id,
        assignment_id=assignment_id,
        course_id=course_id,
        event_id=event_id,
    )
    session.add(task)
    session.commit()
    return task

def delete_task(id: str):
    task = session.query(Task).filter(Task.id == id).first()
    session.delete(task)
    session.commit()
    return task