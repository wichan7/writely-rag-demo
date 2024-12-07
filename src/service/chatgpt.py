from src.core.db import Session
import src.model.chatgpt as chatgpt
from decorator.transactional import transactional
from src.model.document import Document

def query_with_human_message(query: str):
  return chatgpt.query_with_human_message(query)

@transactional
def query_with_embedding(query: str):
  session = Session()

  document_query = session.query(Document)
  documents = [document.content for document in document_query.all()]

  return chatgpt.query_with_embedding(documents, query)