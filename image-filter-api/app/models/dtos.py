from pydantic import BaseModel

class UploadImageDTO(BaseModel):
    filter_name: str

class ProcessedImageDTO(BaseModel):
    id: str
    filter_name: str
    processed_image: bytes