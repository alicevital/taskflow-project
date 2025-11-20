from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    description: str

class Task(BaseModel):
    id: int
    name: str
    datetime: datetime
    status: str
    content: str

