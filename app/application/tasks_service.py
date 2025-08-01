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

    def run(self, task_id: UUID, title: str = None, description: str = None, priority: Priority = None, status: TaskStatus = None):
        task = self.repository.get(task_id)

        if title is not None:
            task.title = title
        if description is not None:
            task.descripcion = description
        if priority is not None:
            task.priority = priority
        if status is not None:
            task.status = status
            if status == TaskStatus.done:
                task.completion_date = datetime.now()

        self.repository.save(task)
        return task


class ListTaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository
    def run(self):
        return self.repository.list_all()
