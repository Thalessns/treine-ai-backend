from fastapi import FastAPI

from src.llm.router import llm_router

app = FastAPI(
    title="Treine.AI - API",
    version="0.1.0"
)

app.include_router(llm_router)
