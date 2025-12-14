'''
Nesse arquivo ficará os schemas do pydantic de validação dos dados
'''
from typing import Optional

class UserRequest:
    username: str
    email: str
    password: str

class UserResponse:
    id: str
    username: str
    email: str
    description: str
    password: str


class TaskRequest:
    user_id: str
    name: str
    difficulty: str
    content: str
    status: str

class TaskResponse:
    id: str
    name: str
    difficulty: str
    content: str
    status: str
    datetime: str