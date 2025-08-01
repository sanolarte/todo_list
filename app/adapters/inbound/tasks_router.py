from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.application.tasks_service import CreateTaskService
from app.adapters.outbound.memory import MemoryRepository
from app.domain.models import Task

router = APIRouter()

class TaskCreationInput(BaseModel):
    title: str
    description: str = ""
    priority: str = "medium"

def get_create_task_service():
    repository = MemoryRepository()
    return CreateTaskService(repository)

@router.post("/", response_model=Task)
def create_task(data: TaskCreationInput, service: CreateTaskService = Depends(get_create_task_service)):
    return service.run(data.title, data.description, data.priority)