from datetime import datetime
from pydantic import BaseModel
from typing import Optional

''' Models Users'''

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    description: str
    password: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {str: str}

class UserLogin(User):
    username: str
    email: str
    password: str


''' Models Tasks '''

class Task(BaseModel):
    id: Optional[str] = None
    name: str
    datetime: datetime
    status: str
    content: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {str: str}

class CreateTask(Task):
    name: str
    status: str
    content: str


''' Models Groups '''

class Group(BaseModel):
    name: str
    description: str
    id: Optional[str] = None
    members: list
    tasks: list

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {str: str}
