'''
Nesse arquivo ficará as rotas de autenticação de login e registro
'''

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

@router.post('/auth/register')
def register_user(user: UserRegister):

    if user.email == "teste@gmail.com":
        raise HTTPException(status_code=400, detail='Usuário já existe')
    return {'message': f'usuário criado com sucesso'}

class UserLogin(BaseModel):
    email: str
    password: str

@router.post('/auth/login')
def login_user(user: UserLogin):
    if user.email != "teste@gmail.com" or user.password != '1234':
        raise HTTPException(status_code=400, detail='Credenciais inválidas')
    
    return {'token': '12345678000'}