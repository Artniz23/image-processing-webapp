from pymongo.results import InsertOneResult

from app.core.db import get_collection
from app.models.dtos import SaveImageDTO


class ImageRepository:
    def __init__(self):
        self.collection = get_collection("images")

    def save_image(self, image: SaveImageDTO):
        result: InsertOneResult = self.collection.insert_one(image.model_dump())
        return str(result.inserted_id)

    def get_image_by_id(self, image_id: str):
        return self.collection.find_one({"_id": image_id})