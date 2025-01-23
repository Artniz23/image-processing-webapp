from pymongo.results import InsertOneResult

from app.models.dtos import SaveImageDTO


class ImageRepository:
    def __init__(self, collection):
        self.collection = collection

    def save_image(self, image: SaveImageDTO):
        result: InsertOneResult = self.collection.insert_one(image.model_dump())
        return str(result.inserted_id)

    def get_image_by_id(self, image_id: str):
        return self.collection.find_one({"_id": image_id})