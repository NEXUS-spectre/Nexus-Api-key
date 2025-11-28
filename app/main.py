# app/main.py
from fastapi import FastAPI
from app.routes import hello, tools, public_api, more_endpoints_soon

app = FastAPI(
    title="Nexus API 🔑",
    description="Your custom multi-endpoint API",
    version="1.0.0"
)

# Include routers
app.include_router(hello.router)
app.include_router(tools.router)
app.include_router(public_api.router)
app.include_router(more_endpoints_soon.router)
