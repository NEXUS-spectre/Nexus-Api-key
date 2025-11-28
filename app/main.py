from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import hello, tools, public_api

app = FastAPI(title="Nexus API 🔑")

# Include routers
app.include_router(hello.router)
app.include_router(tools.router)
app.include_router(public_api.router)

# Root endpoint
@app.get("/")
def root():
    return {"status": "Nexus API 🔑 is running"}

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")