'''
Rotas para o perfil de usuário.
'''
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

router.get('/users/me')
def show_data():
    pass

router.put('/users/me')
def update_data():
    pass

router.delete('/users/me')
def delete_data():
    pass

