from typing import List
from uuid import UUID
from app.domain.models import Task
from app.domain.ports import TaskRepository

class MemoryRepository(TaskRepository):
    def __init__(self):
        self._tasks = {}

    def save(self, task: Task):
        self._tasks[task.id] = task
        
    def get(self, task_id: UUID) -> Task:
        return self._tasks[task_id]
    
    def list_all(self) -> List[Task]:
        import pdb; pdb.set_trace()
        return self._tasks