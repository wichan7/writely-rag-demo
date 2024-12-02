from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/")
def home():
    return os.environ['OPENAI_API_KEY']