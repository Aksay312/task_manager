from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
import enum
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import DateTime
import datetime

# Enum класс для описывающий возможные значения для статуса задач
class  TaskStatus(enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    DONE = "done"

# Модель SQLAlchemy для таблицы "tasks"
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    status = Column(SqlEnum(TaskStatus), default=TaskStatus.NEW)
    description = Column(String(255), nullable=True)
    due_date = Column(DateTime, nullable=True)