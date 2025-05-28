from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

# Здесь описаны все pydantic схемы

# Enum представляющий собой допустымые значения для статуса задачи
class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

# Схема для создания новой задачи
class TaskCreate(BaseModel):
    title:str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Optional[TaskStatus] = TaskStatus.new


# Cхема для обновления статуса задачи
class TaskStatusUpdate(BaseModel):
    status: TaskStatus

# Схема испльзуемая для ответов API
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    due_date: Optional[datetime]

    class Config:
        from_attributes = True # Включаем ORM mode чтобы сериализовать SQLAlchemy модели

# Схема для редактирования задачи
class TaskEdit(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None