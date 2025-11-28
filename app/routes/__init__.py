# app/routes/__init__.py

from fastapi import APIRouter
from .hello import router as hello_router
from .tools import router as tools_router
from .public_api import router as public_router

api_router = APIRouter()

api_router.include_router(hello_router)
api_router.include_router(tools_router)
api_router.include_router(public_router)
