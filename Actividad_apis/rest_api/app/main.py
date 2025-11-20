# main.py
from fastapi import FastAPI
from .database import Base, engine
from .routes import router as api_router
from . import models
import os

app = FastAPI(title="Encuestas - REST API (FastAPI)")

# Crea tablas si no existen (opcional; usa con cuidado si Railway ya tiene esquema)
if os.getenv("INIT_DB", "false").lower() in ("1", "true", "yes"):
    Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api")
