from src.core.db import Session
from src.decorator.transactional import transactional
from src.model.document import Document
from sqlalchemy import select

# get documents
@transactional
def get_documents():
  session = Session()
  documents = session.query(Document).all()

  return [document.as_dict() for document in documents]

# get document
@transactional
def get_document(document_id: int):
  session = Session()
  document = session.execute(
    select(Document).filter_by(id=document_id)
  ).scalar_one()
  
  return document.as_dict()

# create document
@transactional
def create_document(new_document: Document):
  session = Session()
  session.add(new_document)

# update document
@transactional
def modify_document(new_document: Document):
  session = Session()
  
  old_document = session.execute(
    select(Document).filter_by(id=new_document.id)
  ).scalar_one()
  old_document.content = new_document.content

# delete document
@transactional
def remove_document(document_id: int):
  session = Session()

  document = session.execute(
    select(Document).filter_by(id=document_id)
  ).scalar_one()
  session.delete(document)