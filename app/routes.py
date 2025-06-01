from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database
from typing import Optional
from fastapi import Query
from datetime import datetime
from app.dependencies import verify_token

# Создаем объект роутера
router = APIRouter(
    prefix="/api",
    tags=["tasks"],
    dependencies=[Depends(verify_token)]
)

# Функция возвращает объект сессии к БД
def get_db():
    db = database.SessionLocal()
    try:
        yield db 
    finally:
        db.close()


# Роут для возращения задач с опциональной фильтрацией по статусу и по дате
@router.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(
    db: Session = Depends(get_db),
    status: Optional[schemas.TaskStatus] = Query(None),
    due_before: Optional[datetime] = Query(None)
):
    tasks = crud.get_tasks(db, status=status, due_before=due_before)
    return tasks


# Роут для создания задачи
@router.post("/task/create", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


# Удаление задачи
@router.delete("/task/{task_id}/delete", response_model=schemas.TaskDelete)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return schemas.TaskDelete(deleted=True)


# Обновление статуса задачи
@router.patch("/task/{task_id}/status", response_model=schemas.TaskResponse)
def update_task_status(task_id: int, status: schemas.TaskStatusUpdate, db: Session = Depends(get_db)):
    task = crud.update_task_status(db, task_id, status)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task


# Редактирование задачи
@router.patch("/task/{task_id}/edit", response_model=schemas.TaskResponse)
def edit_task(task_id: int, updates: schemas.TaskEdit, db: Session = Depends(get_db)):
    task = crud.edit_task(db, task_id, updates)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task