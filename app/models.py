from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    description: str
    password: str

class CreateUser(User):
    useername: str
    email: str
    password: str

class UserLogin(User):
    username: str
    email: str
    password: str

class Task(BaseModel):
    id: int
    name: str
    datetime: datetime
    status: str
    content: str

class CreateTask(Task):
    name: str
    status: str
    content: str
