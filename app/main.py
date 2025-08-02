# app/main.py
from fastapi import FastAPI
from app.adapters.inbound import tasks_router, lists_router

app = FastAPI()
app.include_router(tasks_router.router, prefix="/task", tags=["Tasks"])
app.include_router(lists_router.router, prefix="/list", tags=["TaskLists"])