from main import session
from database.models import Course, Section, UserSection, section_enum
from datetime import datetime


def get_course(course_code: str, school_id: str):
    course = session.query(Course).filter(Course.course_code == course_code, Course.school_id == school_id).first()

    return course

def get_course_by_id(id: str):
    course = session.query(Course).filter(Course.id == id).first()

    return course

def add_course(
    id: str, 
    course_code: str, 
    name: str, 
    department: str,  
    description: str, 
    units: float,
    school_id: str
):
    course = Course(
        id=id, 
        course_code=course_code, 
        name=name, 
        department=department,
        description=description, 
        units=units,
        school_id=school_id
    )

    session.add(course)
    session.commit()
    return course

def get_section(section_id: str, course_id: str):
    section = session.query(Section).filter(Section.section_id == section_id, Section.course_id == course_id).first()

    return section

def add_section(
    id: str,
    course_id: str,
    section_id: str,
    section_type: section_enum,
    days: str,
    start_time: datetime,
    end_time: datetime,
    instructor_first_name: str,
    instructor_last_name: str,
    instructor_email: str,
    description: str,
    grading_scale: str,
    location: str
):
    section = Section(
        id=id,
        course_id=course_id,
        section_id=section_id,
        section_type=section_type,
        days=days,
        start_time=start_time,
        end_time=end_time,
        instructor_first_name=instructor_first_name,
        instructor_last_name=instructor_last_name,
        instructor_email=instructor_email,
        description=description,
        grading_scale=grading_scale,
        location=location
    )

    session.add(section)
    session.commit()
    return section

def delete_course(id: str):
    course = session.query(Course).filter(Course.id == id).first()
    session.delete(course)
    session.commit()
    return course

def add_user_section(id: str, user_id: str, section_id: str):
    user_section = UserSection(id=id, user_id=user_id, section_id=section_id)
    session.add(user_section)
    session.commit()
    return user_section

def get_user_sections(user_id: str):
    user_sections = session.query(UserSection).filter(UserSection.user_id == user_id).all()
    return user_sections
