from pymongo.results import InsertOneResult

from app.core.db import get_collection

class ImageRepository:
    def __init__(self):
        self.collection = get_collection("images")

    def save_image(self, data: dict):
        result: InsertOneResult = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_image_by_id(self, image_id: str):
        return self.collection.find_one({"_id": image_id})