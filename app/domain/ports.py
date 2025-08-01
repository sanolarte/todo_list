# app/domain/puertos.py
from abc import ABC, abstractmethod
from uuid import UUID
from .models import Task

class TaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task): ...
    @abstractmethod
    def get(self, tarea_id: UUID) -> Task: ...