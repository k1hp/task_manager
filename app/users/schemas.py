from pydantic import BaseModel, EmailStr
from app.models import Task

class UserCreateSchema(BaseModel):
    name: str
    password: str
    # email: EmailStr
    # fisting: int


class UserResponseSchema(BaseModel):
    name: str
    password: str
    email: EmailStr
    # tasks: list["Task"]