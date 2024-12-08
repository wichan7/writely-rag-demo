import src.model.chatgpt as chatgpt
from src.core.db import Session
from src.decorator.transactional import transactional
from src.model.document import Document

def query_with_human_message(query: str):
  result = chatgpt.query_with_human_message(query)
  return result

@transactional
def query_with_embedding(query: str):
  session = Session()

  document_query = session.query(Document)
  documents = [document.content for document in document_query.all()]

  result = chatgpt.query_with_embedding(documents, query)

  return result