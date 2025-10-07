from dataclasses import dataclass

from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
from typing import Literal


@dataclass
class Header:
    alg: str = "HS256"
    typ: str = "JWT"

class Payload(BaseModel):
    sub: str
    email: EmailStr
    iat: datetime
    exp: datetime
    type: Literal["access", "refresh"]


import jwt
from datetime import datetime, timedelta

# Создание JWT
payload = {
    "sub": "user_123",
    "email": "user@taskmanager.com",
    "iat": (datetime.now() - timedelta(minutes=10)).timestamp(),
    "exp": (datetime.now() + timedelta(minutes=30)).timestamp(),
    "type": "access"
}

secret = "your-secret-key"

token = jwt.encode(payload, secret, algorithm=Header.alg)
print("PyJWT token:")
print(token)

response = jwt.decode(token, secret, algorithms=[Header.alg])

print(response)
payload = Payload(**response)
print(payload)

class HashedPassword(str):
    def __new__(cls, value):
        return super().__new__(cls, cls.convert(value))

    @staticmethod
    def convert(value: str) -> str:
        return value * 2

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def hash_password(cls, value: str) -> str:
        return HashedPassword(value)

request = LoginSchema(email="email@gmail.com", password="<PASSWORD>")
print(request)