from typing import List
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.messages import HumanMessage
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

chat_model = ChatOpenAI(model='gpt-3.5-turbo')
embedding_model = OpenAIEmbeddings(model='text-embedding-3-small')

def query_with_human_message(query: str):
  response = chat_model.invoke([HumanMessage(content=query)])
  return response.content

def query_with_embedding(documents: List[str], query: str):
  print("Documents:", documents)
  document_embeddings = embedding_model.embed_documents(documents)
  query_embedding = embedding_model.embed_query(query)

  similarities = cosine_similarity([query_embedding], document_embeddings)[0]
  most_similar_index = np.argmax(similarities)

  print("Query:", query)
  print("Most similar document:", documents[most_similar_index])
  print("Similarity score:", similarities[most_similar_index])

  return