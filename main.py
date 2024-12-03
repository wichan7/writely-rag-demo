from src.core.env import load_env
load_env()
from fastapi import FastAPI
from src.router.default import router as default_router
from src.router.product import router as product_router
from src.router.chatgpt import router as chatgpt_router

app = FastAPI()
app.include_router(default_router, prefix="")
app.include_router(product_router, prefix="/v1/products")
app.include_router(chatgpt_router, prefix="/v1/chatgpt")