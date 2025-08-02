# app/domain/puertos.py
from abc import ABC, abstractmethod
from uuid import UUID
from .models import Task, TaskList

class TaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task): ...
    @abstractmethod
    def get(self, tarea_id: UUID) -> Task: ...


class TaskListRepository(ABC):
    @abstractmethod
    def save(self, list: TaskList): ...

    @abstractmethod
    def get(self, list_id: UUID) -> TaskList: ...

    @abstractmethod
    def delete(self, list_id: UUID): ...

    @abstractmethod
    def list(self) -> list[TaskList]: ...