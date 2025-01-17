from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME]

def get_collection(collection_name: str):
    return db[collection_name]