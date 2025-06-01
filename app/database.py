from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Путь до файла БД
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"


# Настройка движка SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# Создание сессии к БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Базовый класс для создания SQLAlchemy моделей
# Все модели наследуются от этого класса
Base = declarative_base()