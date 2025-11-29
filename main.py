from fastapi import FastAPI

from app.routers import auth, users, tasks # Importa os arquivos de rotas

app = FastAPI()

app.include_router(auth.router) #registra as rotas de cada um dos arquivos
app.include_router(users.router) # o include_router faz o fastapi reconhecer as rotas que estão dentro dos arquivos
app.include_router(tasks.router)

@app.get('/')
def root():
    return {'message': 'Bem-vindo ao Taskflow'}