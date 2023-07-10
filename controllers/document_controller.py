from main import session
from database.models import Document

from datetime import datetime

# TODO: add crud for documents, building off upload_document endpoint
def get_document(id: str):
    document = session.query(Document).filter(Document.id == id).first()

    return document

def get_documents(user_id: str):
    documents = session.query(Document).filter(Document.user_id == user_id).all()

    return documents

def add_document(
    id: str, 
    name: str, 
    type: str, 
    url: str, 
    section_id: str, 
    assignment_id: str, 
    user_id: str
):
    document = Document(
        id=id, 
        name=name, 
        type=type, 
        url=url, 
        section_id=section_id, 
        assignment_id=assignment_id, 
        user_id=user_id
    )
    session.add(document)
    session.commit()
    return document

def delete_document(id: str):
    document = session.query(Document).filter(Document.id == id).first()
    session.delete(document)
    session.commit()
    return document