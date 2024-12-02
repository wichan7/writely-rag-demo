from fastapi import APIRouter
import src.service.chatgpt as chatgpt_service

router = APIRouter()

@router.get("/human")
def query(query: str = ''):
    return chatgpt_service.query_with_human_message(query)

@router.get("/embedding")
def query(query: str = ''):
    return chatgpt_service.query_with_embedding(query)