from pydantic import BaseModel

class ProcessImageResponseDTO(BaseModel):
    id: str
    message: str

class SaveImageDTO(BaseModel):
    filter_name: str
    original_image: bytes
    processed_image: bytes