# Task Manager API

Простой REST API для управления задачами.  
Реализовано на FastAPI, с использованием SQLAlchemy и Pydantic.

## Возможности

- Создание задач с полями: `title`, `description`, `due_date`, `status`
- Обновление статуса и описания задач
- Удаление задач
- Фильтрация по `status` и `due_date`
- Авторизация через токен в заголовке `Authorization: Bearer <token>`
- Swagger-документация

## Технологии

- Python 3.13.2
- FastAPI  0.115.12
- SQLAlchemy 2.0.41  
- Pydantic 2.11.4  
- SQLite

## Авторизация

Требуется заголовок:
"mysecrettoken"



Swagger поддерживает авторизацию через кнопку **"Authorize"**.

## Установка и запуск

```bash
git clone <repo-url>
cd task_manager
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

После запуска перейти в браузер
http://localhost:8000/docs

