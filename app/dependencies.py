from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Схема безопасности
security = HTTPBearer()


# функция для проверки токена в загаловке запроса
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer" or credentials.credentials != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Invalid or missing token")
