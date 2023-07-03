from main import session
from database.models import School

def get_school(id: str):
    school = session.query(School).filter(School.id == id).first()

    return school

def add_school(id: str, name: str):
    school = School(id=id, name=name)
    session.add(school)
    session.commit()

    return school

def delete_school(id: str):
    school = session.query(School).filter(School.id == id).first()
    session.delete(school)
    session.commit()

    return school