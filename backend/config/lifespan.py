from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import init_db
# lifespan handles startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await init_db()
    print("Database connected")
    yield
    # shutdown (optional cleanup)
    print("App shutting down")