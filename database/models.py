from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text, TIMESTAMP, TIME
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ENUM as PGENUM
from enum import Enum

Base = declarative_base()

class section_enum(Enum):
    Lecture = "Lecture"
    Discussion = "Discussion"
    Quiz = "Quiz"

class status_enum(Enum):
    TODO = "TODO"
    INPROGRESS = "INPROGRESS"
    COMPLETE = "COMPLETE"


class School(Base):
    __tablename__ = 'schools'

    id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    school_id = Column(String, ForeignKey('schools.id'))
    school = relationship("School")

    def __init__(self, id: str, first_name: str, last_name: str, email: str, password: str, school_id: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.school_id = school_id


class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True)
    course_code = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    description = Column(Text)
    units = Column(Float)
    school_id = Column(String, ForeignKey('schools.id'))
    school = relationship("School")

class Section(Base):
    __tablename__ = 'sections'

    id = Column(String, primary_key=True)
    section_id = Column(String(100), nullable=False)
    section_type = Column(PGENUM(section_enum, name='section_enum'), nullable=False)
    days = Column(String(100), nullable=False)
    start_time = Column(TIME, nullable=False)
    end_time = Column(TIME, nullable=False)
    instructor_first_name = Column(String(100), nullable=False)
    instructor_last_name = Column(String(100), nullable=False)
    instructor_email = Column(String(100))
    description = Column(Text)
    grading_scale = Column(Text)
    location = Column(String(100))
    course_id = Column(String, ForeignKey('courses.id'))
    course = relationship("Course")


class UserSection(Base):
    __tablename__ = 'user_sections'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    section_id = Column(String, ForeignKey('sections.id'))
    user = relationship("User")
    section = relationship("Section")

class Assignment(Base):
    __tablename__ = 'assignments'

    id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)
    due_date = Column(TIMESTAMP, nullable=False)
    status = Column(PGENUM(status_enum, name='status_enum'), nullable=False)
    description = Column(Text)
    priority = Column(Integer)
    section_id = Column(String, ForeignKey('sections.id'))
    user_id = Column(String, ForeignKey('users.id'))
    section= relationship("Section")
    user = relationship("User")


class Document(Base):
    __tablename__ = 'documents'

    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)
    url = Column(Text, nullable=False)
    section_id = Column(String, ForeignKey('sections.id'))
    assignment_id = Column(String, ForeignKey('assignments.id'))
    user_id = Column(String, ForeignKey('users.id'))
    section = relationship("Section")
    assignment = relationship("Assignment")
    user = relationship("User")


class Event(Base):
    __tablename__ = 'events'

    id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)
    start_time = Column(TIMESTAMP, nullable=False)
    end_time = Column(TIMESTAMP)
    description = Column(Text)
    priority = Column(Integer)
    section_id = Column(String, ForeignKey('sections.id'))
    user_id = Column(String, ForeignKey('users.id'))
    section = relationship("Section")
    user = relationship("User")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    status = Column(PGENUM(status_enum, name='status_enum'), nullable=False)
    description = Column(Text)
    priority = Column(Integer)
    assignment_id = Column(String, ForeignKey('assignments.id'))
    section_id = Column(String, ForeignKey('sections.id'))
    event_id = Column(String, ForeignKey('events.id'))
    user_id = Column(String, ForeignKey('users.id'))
    assignment = relationship("Assignment")
    section = relationship("Section")
    event = relationship("Event")
    user = relationship("User")
