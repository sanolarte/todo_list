from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.application.tasks_service import CreateTaskService, UpdateTaskService, ListTaskService
from app.adapters.outbound.memory import MemoryRepository
from app.domain.models import Task, Priority, TaskStatus

router = APIRouter()

class TaskCreationInput(BaseModel):
    title: str
    description: str = ""
    priority: str = "medium"

class UpdateTaskInput(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: Priority | None = None
    status: TaskStatus | None = None

def get_create_task_service():
    repository = MemoryRepository()
    return CreateTaskService(repository)

def get_update_task_service():
    repository = MemoryRepository()
    return UpdateTaskService(repository)

def get_list_task_service():
    repository = MemoryRepository()
    return ListTaskService(repository)

@router.post("/", response_model=Task)
def create_task(data: TaskCreationInput, service: CreateTaskService = Depends(get_create_task_service)):
    return service.run(data.title, data.description, data.priority)

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: UUID, data: UpdateTaskInput, service: UpdateTaskService = Depends(get_update_task_service)):
    return service.run(
        task_id,
        title=data.title,
        description=data.description,
        priority=data.priority,
        status=data.status
    )

@router.get("/", response_model=List[Task])
def list_tasks(service: ListTaskService = Depends(get_list_task_service)):
    return service.run()
