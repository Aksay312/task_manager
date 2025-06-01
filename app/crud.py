from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime
from typing import Optional

# Тут описана вся логика взаимодествия с базой данных


# Получает задачи из базы данных. Опцианольно фильтрует по статусу и по дате
def get_tasks(db: Session, status: Optional[schemas.TaskStatus] = None, due_before: Optional[datetime] = None):
    query = db.query(models.Task)
    if status:
        query = query.filter(models.Task.status == models.TaskStatus(status.value))
    if due_before:
        query = query.filter(models.Task.due_date <= due_before)
    return query.all()


# Вспомогательная функция для получения одной задачи по id
def get_task_by_id(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return db_task


# Создаем задачу с валидированными по схеме данными
# Сохраняем в БД и возвращаем задачу
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title, 
        description=task.description, 
        status=models.TaskStatus(task.status.value),
        due_date=task.due_date
        )
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# Удаление задачи по id. Возвращает true если удалено. Если задача не найдена возаращает None
def delete_task(db: Session, task_id: int):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()

    return True


# Обновление статуса задачи
# Возвращает обновленную задачу или None если задача не найдена
def update_task_status(db: Session, task_id: int, status_update: schemas.TaskStatusUpdate):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return None
    db_task.status = models.TaskStatus(status_update.status.value)
    db.commit()
    db.refresh(db_task)
    return db_task


# Частично обновляет такие поля как: title, description и due_date
# Возвращает обновленную задачу или None если задача не найдено
def edit_task(db: Session, task_id: int, updates: schemas.TaskEdit):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return None
    if updates.title is not None:
        db_task.title = updates.title
    if updates.description is not None:
        db_task.description = updates.description
    if updates.due_date is not None:
        db_task.due_date = updates.due_date

    db.commit()
    db.refresh(db_task)
    return db_task