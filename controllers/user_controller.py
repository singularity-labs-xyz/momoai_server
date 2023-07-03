
from main import session
from database.models import User

def get_user(id: str):
    user = session.query(User).filter(User.id == id).first()
    return user

def add_user(id: str, first_name: str, last_name: str, email: str, password: str, school_id: str):
    user = User(id=id, first_name=first_name, last_name=last_name, email=email, password=password, school_id=school_id)
    session.add(user)
    session.commit()
    return user

def delete_user(id: str):
    user = session.query(User).filter(User.id == id).first()
    session.delete(user)
    session.commit()
    return user