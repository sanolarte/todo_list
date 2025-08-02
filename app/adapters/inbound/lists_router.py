from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.application.list_service import CreateListService
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


@router.post("/", response_model=TaskListModel)
def create_list(data: CreateListInput, service: CreateListService = Depends(get_create_list_service)):
    return service.run(data)
