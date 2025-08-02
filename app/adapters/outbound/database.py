from uuid import UUID, uuid4
from typing import List

from datetime import datetime
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select, Column, Relationship
from sqlalchemy import DateTime, func

from app.domain.models import Task as TaskModel
from app.domain.models import TaskList as TaskListModel
from app.domain.models import TaskStatus
from app.domain.ports import TaskRepository, TaskListRepository


class TaskList(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    tasks: List["Task"] = Relationship(back_populates="task_list")

class Task(SQLModel, table=True):
    id: UUID  = Field(default_factory=uuid4, primary_key=True)
    title: str
    description: Optional[str]
    priority: Optional[str]
    status: Optional[str]
    completion_date: Optional[datetime]
    created_at: datetime = Field(sa_column=Column(DateTime(), server_default=func.now()))
    updated_at: Optional[datetime] = Field(sa_column=Column(DateTime(), onupdate=func.now()))

    task_list_id: Optional[UUID] = Field(foreign_key="tasklist.id")

    task_list: Optional[TaskList] = Relationship(back_populates="tasks")


class TaskDatabaseRepository(TaskRepository):
    def __init__(self):
        self.engine = create_engine("sqlite:///database.db")
        SQLModel.metadata.create_all(self.engine)

    def save(self, task: Task):
        task_obj = Task(**task.dict())
        with Session(self.engine) as session:
            session.add(task_obj)
            session.commit()
    

    def update(self, task_id: UUID, data):
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
            if data.title:
                task.title = data.title
            if data.description:
                task.description = data.description
            if data.priority:
                task.priority = data.priority
            if data.status:
                task.status = data.status
                if data.status == TaskStatus.done:
                    task.completion_date = datetime.now()
            session.add(task)
            session.commit()
            session.refresh(task)
        return task

    def get(self, task_id: UUID) -> Task:
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
        return task
    
    def list_all(self) -> List[TaskModel]:
        with Session(self.engine) as session:
            statement = select(Task)
            tasks = session.exec(statement)
            return [TaskModel.from_orm(task) for task in tasks]
        


class TaskListDatabaseRepository(TaskListRepository):
    def __init__(self):
        self.engine = create_engine("sqlite:///database.db")
        SQLModel.metadata.create_all(self.engine)
    
    def save(self, task_list: TaskList):
        list_dict = task_list.dict()

        new_list = TaskList(name=task_list.name)
        if list_dict.get("tasks"):
            new_list.tasks = [Task(**task, task_list_id=new_list.id) for task in list_dict["tasks"]]

        with Session(self.engine) as session:
            session.add(new_list)
            session.commit()

    
    def delete(self):
        pass
    
    def get(self):
        pass
    
    def list(self):
        with Session(self.engine) as session:
            statement = select(TaskList)
            lists = session.exec(statement)
            return [TaskListModel.from_orm(list) for list in lists]


