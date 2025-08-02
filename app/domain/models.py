from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(BaseModel):
    id: UUID = uuid4()
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending
    prioridad: Priority = Priority.medium
    creation_date: datetime = datetime.now()
    completion_date: Optional[datetime] = None

    class Config:
        from_attributes=True
        orm_mode = True


class TaskList(BaseModel):
    id: UUID = uuid4()
    name: str
    tasks: List[Task] = []
    
    class Config:
        from_attributes=True
