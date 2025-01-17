from pydantic import BaseModel
from bson import ObjectId

class ImageEntity(BaseModel):
    id: str
    filter_name: str
    original_image: bytes
    processed_image: bytes

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}