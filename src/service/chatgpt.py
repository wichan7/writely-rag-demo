import src.model.chatgpt as chatgpt
from src.model.document import Document
from src.core.db import session_factory

def query_with_human_message(query: str):
  return chatgpt.query_with_human_message(query)

def query_with_embedding(query: str):
  session = session_factory()

  document_query = session.query(Document)
  documents = [document.content for document in document_query.all()]

  return chatgpt.query_with_embedding(documents, query)