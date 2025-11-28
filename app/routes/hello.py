# app/routes/hello.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["Hello"]
)

@router.get("/")
async def say_hello(name: str = "User"):
    return {"message": f"Hello, {name}!", "status": "success"}