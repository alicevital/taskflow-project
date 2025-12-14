from fastapi import FastAPI

from app.routers import auth_router, task_router, users_router # Importa os arquivos de rotas

app = FastAPI()

app.include_router(auth_router.router) #registra as rotas de cada um dos arquivos
app.include_router(users_router.router) # o include_router faz o fastapi reconhecer as rotas que estão dentro dos arquivos
app.include_router(task_router.router)

@app.get('/')
def root():
    return {'message': 'Bem-vindo ao Taskflow'}