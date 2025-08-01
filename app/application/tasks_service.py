from uuid import uuid4
from app.domain.models import Task
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
