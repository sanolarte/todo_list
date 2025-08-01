# app/adapters/outbound/repositorios_memoria.py
from uuid import UUID
from app.domain.models import Task
from app.domain.ports import TaskRepository

class MemoryRepository(TaskRepository):
    def __init__(self):
        self._tasks = {}

    def save(self, task: Task):
        self._tasks[task.id] = task

    def update(self, task: Task):
        pass
    def get(self, task_id: UUID) -> Task:
        return self._tasks[task_id]