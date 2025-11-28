# app/routes/tools.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/tools",
    tags=["Tools"]
)

@router.get("/ping")
async def ping():
    return {"message": "pong", "status": "success"}

@router.get("/add")
async def add(a: int, b: int):
    return {"result": a + b, "status": "success"}

@router.get("/subtract")
async def subtract(a: int, b: int):
    return {"result": a - b, "status": "success"}
