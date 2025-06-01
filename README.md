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

Токен для авторизации: mysecrettoken

Swagger поддерживает авторизацию через кнопку **"Authorize"**.

## Установка и запуск

git clone <repo-url>

cd task_manager

python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload


Полсе запуска перейти в браузер

http://localhost:8000/docs

## Эндпоинты

GET	    /api/tasks

POST	/api/task/create

DELETE	/api/task/{task_id}/delete

PATCH	/api/task/{task_id}/status

PATCH	/api/task/{task_id}/edit

## Примеры запросов
Создать задачу:

    POST http://127.0.0.1:8000/api/task/create
    Authorization: Bearer mysecrettoken
    Content-Type: application/json

    {
    "title": "Buy milk",
    "description": "From the store",
    "status": "new",
    "due_date": "2025-06-01T12:00:00"
    }


Вывести задачи с опциональной фильтрацией:

    GET http://127.0.0.1:8000/api/tasks?status=new&due_before=2025-06-25T00:00:00
    Authorization: Bearer mysecrettoken



Редактировать задачу:

    PATCH http://127.0.0.1:8000/api/task/1/edit
    Authorization: Bearer mysecrettoken
    Content-Type: application/json

    {
    "description": "Updated desc",
    "due_date": "2025-06-10T15:00:00"
    }

Обновление статуча задачи:

    PATCH http://127.0.0.1:8000/api/task/1/status
    Authorization: Bearer mysecrettoken
    Content-Type: application/json

    {
    "status": "done"
    }

Удаление задачи:

    DELETE http://127.0.0.1:8000/api/task/1/delete
    Authorization: Bearer mysecrettoken



##  Пример на postman

Создать задачу:
![image](https://github.com/user-attachments/assets/2ade8b2d-33b1-400f-b61a-a12925c3816c)

Вывод задачи с фильтрацией:
![image](https://github.com/user-attachments/assets/9a5f25cd-b8fa-4684-a011-3ae8364d2ad8)

Редактирования задачи:
![image](https://github.com/user-attachments/assets/11847859-a736-4a30-97a1-cd1b8a77dfc6)

Удаление задачи:
![image](https://github.com/user-attachments/assets/cd5a4543-3eda-41fa-8118-63be9316ce86)













##  Рефлексии
1. Что было самым сложным?
Разобраться как работать с базой данных и как эту штуку запушить в чертов github. 

2. Что получилось особенно хорошо?
Гибкая фильтрация, чистая архитектура, авторизация через токен.

3. Что бы я доработал?
Роли (admin / user), docker-файл, и unit-тесты. Но пока не знаю как писать тесты и знаю что такое docker

4. Сколько времени заняло выполнение?
3-4 дня (и психотерапия после этого).

5. Чему я научился?
Понял что такое FastAPI, запросы, и REST в целом. Научился коммитить и пушить проект в github, хоть и все еще не понимаю многих приколов этой штуки. Думаю после этого проекта я уже могу строить простые crud приложения хоть и не без помощи google и chat gpt.
