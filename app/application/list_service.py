from typing import List

from uuid import uuid4, UUID
from app.domain.models import TaskList, Task
from app.domain.ports import TaskListRepository, TaskRepository


class CreateListService:
    def __init__(self, repository: TaskListRepository):
        self.repository = repository
    
    def run(self, data) -> TaskList:
        new_list = TaskList(id=uuid4(), name=data.name, tasks=data.tasks)
        self.repository.save(new_list)
        return new_list
    

class ListListService:
    def __init__(self, repository: TaskListRepository):
        self.repository = repository
    
    def run(self) -> TaskList:
        lists = self.repository.list()
        return lists
    

class AddTaskToListService:
    def __init__(self, repository: TaskListRepository, task_repository: TaskRepository):
        self.repository = repository
        self.task_repository = task_repository
    
    def run(self, task_list_id: UUID, tasks: List[dict]) -> TaskList:
        new_tasks = []
        for task in tasks:
            new_task_dict = task.dict()
            new_task = Task(**new_task_dict, task_list_id=task_list_id)
            self.task_repository.save(new_task)
            new_tasks.append(task)