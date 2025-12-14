'''
Nesse arquivo ficará a conexão com o banco de dados.
'''
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB_NAME", "taskflow_db")

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

def get_database():
    return database
