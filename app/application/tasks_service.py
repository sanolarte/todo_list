import datetime
from uuid import uuid4, UUID
from app.domain.models import Task, TaskStatus, Priority
from app.domain.ports import TaskRepository

class CreateTaskService:
        def __init__(self, repository: TaskRepository):
            self.repository = repository

        def run(self, title: str, description: str = "", priority: str = "medium") -> Task:
            new_task = Task(
                id=uuid4(),
                title=title,
                description=description,
                priority=priority
            )
            self.repository.save(new_task)
            return new_task


class UpdateTaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def run(self, task_id: UUID, data):

        updated_task = self.repository.update(task_id, data)
        return updated_task

class ListTaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository
    def run(self):
        return self.repository.list_all()
