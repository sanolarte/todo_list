from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.application.list_service import CreateListService, ListListService
from app.adapters.outbound.database import TaskListDatabaseRepository

from app.domain.models import TaskList as TaskListModel

from .tasks_router import TaskCreationInput


router = APIRouter()

class CreateListInput(BaseModel):
    name: str
    tasks: list[TaskCreationInput]


def get_create_list_service():
    repository = TaskListDatabaseRepository()
    return CreateListService(repository)


def get_list_list_service():
    repository = TaskListDatabaseRepository()
    return ListListService(repository)

@router.post("/", response_model=TaskListModel)
def create_list(data: CreateListInput, service: CreateListService = Depends(get_create_list_service)):
    return service.run(data)


@router.get("/", response_model=List[TaskListModel])
def list_all_lists(service: ListListService = Depends(get_list_list_service)):
    return service.run()
