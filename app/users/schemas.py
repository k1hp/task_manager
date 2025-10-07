from pydantic import BaseModel, EmailStr, computed_field, field_validator
from app.models import Task

class HashedPassword(str):
    def __new__(cls, value):
        return super().__new__(cls, cls.convert(value))

    @staticmethod
    def convert(value: str) -> str:
        return value * 2




class UserCreateSchema(BaseModel):
    name: str
    password: str

    @field_validator("password")
    @classmethod
    def password(cls, value: str):
        return HashedPassword(value)

    # email: EmailStr
    # fisting: int


class UserResponseSchema(BaseModel):
    name: str
    password: str
    email: EmailStr
    # tasks: list["Task"]


if __name__ == '__main__':
    user = UserCreateSchema(name="finger", password="123")
    print(user.model_dump())
    # pwd = HashedPassword('finger')
    # print(pwd)