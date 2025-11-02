'''
Nesse arquivo ficará as rotas das tarefas (Listar, Criar, Atualizar e Deletar).
'''
from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)
class PostRegister(BaseModel):
    title: str
    description: str
    author: str

router.post('/tasks/')
def write_tasks():
    pass

router.get('/tasks/')
def show_tasks():
    pass

router.get('/tasks/{id}')
def show_id_tasks():
    pass

router.put('/tasks/{id}')
def update_tasks():
    pass

router.delete('/tasks/{id}')
def delete_tasks():
    pass