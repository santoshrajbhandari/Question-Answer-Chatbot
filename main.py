from fastapi import FastAPI
from app.api import router

app = FastAPI(title="QA Chatbot API")

app.include_router(router)
