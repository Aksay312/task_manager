from fastapi import FastAPI
from app import models, database
from app.routes import router

# Создаем таблицы в БД
models.Base.metadata.create_all(bind=database.engine)

# Создаем наше fastAPI приложение с описанием
app = FastAPI(
    title="Task Manager API",
    description="Simple task manager using FastAPI, Pydantic and SQLAlchemy",
    version="0.1.0"
)

# Регистрируем роуты
app.include_router(router)