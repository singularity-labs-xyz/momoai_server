import uuid

from pydantic import BaseModel
from fastapi import APIRouter
from momoai_core import logging
from controllers import course_controller
from typing import List
from database.models import section_enum
from datetime import time

router = APIRouter(prefix="/courses")

@router.get("/{course_id}")
def getCourse(course_id: str):
    course = course_controller.get_course_by_id(id=course_id)

    return {
        "id": course.id,
        "course_code:": course.course_code,
        "section_id": course.section_id,
        "name": course.name,
        "department": course.department,
        "professor_name": course.professor_name,
        "professor_email": course.professor_email,
        "description": course.description,
        "school_id": course.school_id
    }

class CourseArgs(BaseModel):
    course_code: str
    name: str
    department: str
    description: str
    units: float
    school_id: str

class SectionArgs(BaseModel):
    section_id: str
    section_type: section_enum
    days: str
    start_time: time
    end_time: time
    instructor_first_name: str
    instructor_last_name: str
    instructor_email: str
    description: str
    grading_scale: str
    location: str

class AddCourseRequestArgs(BaseModel):
    course: CourseArgs
    sections: List[SectionArgs]
    user_id: str

@router.post("/add")
def addCourse(body: AddCourseRequestArgs):
    course = course_controller.get_course(
        course_code=body.course.course_code, 
        school_id=body.course.school_id
    )

    if(course == None):
        course = course_controller.add_course(
            id=str(uuid.uuid4()), 
            course_code=body.course.course_code, 
            name=body.course.name, 
            department=body.course.department, 
            description=body.course.description, 
            units=body.course.units, 
            school_id=body.course.school_id
        )
        logging.info(f"Added course {course.name} with id {course.id}")
    else:
        logging.info(f"Found existing {course.name} with id {course.id}")

    sections = []

    for section_args in body.sections:
        section = course_controller.get_section(section_id=section_args.section_id, course_id=course.id)

        if(section == None):
            section = course_controller.add_section(
                id=str(uuid.uuid4()),
                course_id=course.id,
                section_id=section_args.section_id,
                section_type=section_args.section_type,
                days=section_args.days,
                start_time=section_args.start_time,
                end_time=section_args.end_time,
                instructor_first_name=section_args.instructor_first_name,
                instructor_last_name=section_args.instructor_last_name,
                instructor_email=section_args.instructor_email,
                description=section_args.description,
                grading_scale=section_args.grading_scale,
                location=section_args.location
            )
            logging.info(f"Added section {section.section_id} with id {section.id}")
        else:
            logging.info(f"Found existing {section.section_id} with id {section.id}")

        sections.append(section)

        course_controller.add_user_section(id=str(uuid.uuid4()), user_id=body.user_id, section_id=section.id)

    return{
        "course_id": course.id,
        "course_name": course.name,
        "course_code": course.course_code,
        "course_department": course.department,
        "course_description": course.description,
        "course_units": course.units,
        "course_school_id": course.school_id,
        "section_ids": [section.id for section in sections]
    }

@router.delete("/{course_id}")
def deleteCourse(course_id: str):
    course_controller.delete_course(id=course_id)
    logging.info(f"Deleted course with id {course_id}")
    return{"message": "Course deleted successfully"}

@router.get("/user/{user_id}")
def getCoursesByUserId(user_id: str):
    user_courses = course_controller.get_user_sections(user_id=user_id)

    courses = []

    for user_course in user_courses:
        courses.append(course_controller.get_course_by_id(id=user_course.section.course_id))
    

    return {
        "courses": courses
    }
