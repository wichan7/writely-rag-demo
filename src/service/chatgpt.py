import src.model.chatgpt as chatgpt

def query_with_human_message(query: str):
  return chatgpt.query_with_human_message(query)

def query_with_embedding(query: str):
  return chatgpt.query_with_embedding(query)