# app/main.py
from fastapi import FastAPI
from app.adapters.inbound import tasks_router

app = FastAPI()
app.include_router(tasks_router.router, prefix="/task", tags=["Tasks"])
