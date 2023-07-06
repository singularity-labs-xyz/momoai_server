import uuid

from pydantic import BaseModel
from fastapi import APIRouter
from momoai_core import logging
from controllers import course_controller

router = APIRouter(prefix="/courses")

@router.get("/{course_id}")
def getCourse(course_id: str):
    course = course_controller.get_course_by_id(id=course_id)

    return {
        "id": course.id,
        "course_code:": course.course_code,
        "name": course.name,
        "department": course.department,
        "professor_name": course.professor_name,
        "professor_email": course.professor_email,
        "description": course.description,
        "school_id": course.school_id
    }

class AddCourseRequestArgs(BaseModel):
    course_code: str
    name: str
    department: str
    professor_name: str
    professor_email: str
    description: str
    school_id: str

@router.post("/add")
def addSchool(body: AddCourseRequestArgs):

    # TODO: Check if same exact course exists already, if so just create a new user_course
    course = course_controller.add_course(id=str(uuid.uuid4()), course_code=body.course_code, name=body.name, department=body.department, professor_name=body.professor_name, professor_email=body.professor_email, description=body.description, school_id=body.school_id)
    logging.info(f"Added course {course.name} with id {course.id}")

    # TODO: create a user_course

    return{
        "id": course.id,
        "course_code:": course.course_code,
        "name": course.name,
        "department": course.department,
        "professor_name": course.professor_name,
        "professor_email": course.professor_email,
        "description": course.description,
        "school_id": course.school_id
    }

@router.delete("/{course_id}")
def deleteCourse(course_id: str):
    course_controller.delete_course(id=course_id)
    logging.info(f"Deleted course with id {course_id}")
    return{"message": "Course deleted successfully"}
