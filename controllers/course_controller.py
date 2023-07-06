from main import session
from database.models import Course

def get_course_by_id(id: str):
    course = session.query(Course).filter(Course.id == id).first()

    return course

def add_course(id: str, course_code: str, name: str, department: str, professor_name: str, professor_email: str, description: str, school_id: str):
    course = Course(id=id, course_code=course_code, name=name, department=department, professor_name=professor_name, professor_email=professor_email, description=description, school_id=school_id)
    session.add(course)
    session.commit()
    return course

def delete_course(id: str):
    course = session.query(Course).filter(Course.id == id).first()
    session.delete(course)
    session.commit()

    return course