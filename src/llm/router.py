from fastapi import APIRouter, status

from src.llm.client import client

llm_router = APIRouter(prefix="/llm")


@llm_router.post("/teste", status_code=status.HTTP_201_CREATED)
async def submit():
    return await client.request_gemini()