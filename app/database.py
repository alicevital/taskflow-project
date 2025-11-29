'''
Nesse arquivo ficará a conexão com o banco de dados.
'''
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
cliente = AsyncIOMotorClient(MONGO_URL)

database = cliente.fastapi

