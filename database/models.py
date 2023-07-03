from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class School(Base):
    __tablename__ = 'school'

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
    school_id = Column(String, ForeignKey('school.id'))
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
    professor_name = Column(String(100))
    professor_email = Column(String(100))
    description = Column(Text)
    school_id = Column(String, ForeignKey('school.id'))
    school = relationship("School")


class UserCourse(Base):
    __tablename__ = 'user_courses'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    user = relationship("User")
    course = relationship("Course")


class Document(Base):
    __tablename__ = 'documents'

    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)
    url = Column(String(255), nullable=False)
    class_id = Column(String, ForeignKey('courses.id'))
    assignment_id = Column(String, ForeignKey('assignments.id'))
    user_id = Column(String, ForeignKey('users.id'))
    course = relationship("Course")
    assignment = relationship("Assignment")
    user = relationship("User")


class Event(Base):
    __tablename__ = 'events'

    id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)
    start_time = Column(TIMESTAMP, nullable=False)
    description = Column(Text)
    end_time = Column(TIMESTAMP)
    priority = Column(Integer)
    course_id = Column(String, ForeignKey('courses.id'))
    course = relationship("Course")


class Assignment(Base):
    __tablename__ = 'assignments'

    id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)
    due_date = Column(TIMESTAMP, nullable=False)
    description = Column(Text)
    priority = Column(Integer)
    completed = Column(Boolean)
    course_id = Column(String, ForeignKey('courses.id'))
    course = relationship("Course")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    description = Column(Text)
    priority = Column(Integer)
    completed = Column(Boolean)
    assignment_id = Column(String, ForeignKey('assignments.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    event_id = Column(String, ForeignKey('events.id'))
    assignment = relationship("Assignment")
    course = relationship("Course")
    event = relationship("Event")
