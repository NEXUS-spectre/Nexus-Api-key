# app/routes/public_api.py
from fastapi import APIRouter
import requests

router = APIRouter(
    prefix="/public",
    tags=["Public API"]
)

@router.get("/joke")
async def get_joke():
    """Fetch a random joke from official-joke-api"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        return {"joke": data, "status": "success"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
