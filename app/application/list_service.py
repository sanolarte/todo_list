from uuid import uuid4
from app.domain.models import TaskList
from app.domain.ports import TaskListRepository


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