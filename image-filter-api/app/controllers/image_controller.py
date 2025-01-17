from fastapi import APIRouter, UploadFile, HTTPException
from app.services.image_service import ImageService
from app.repositories.image_repository import ImageRepository

router = APIRouter()
repository = ImageRepository()
service = ImageService(repository)

@router.post("/process")
async def process_image(filter_name: str, file: UploadFile):
    try:
        original_image = await file.read()
        processed_image = service.process_image(filter_name, original_image)
        image_id = service.save_processed_image(filter_name, original_image, processed_image)
        return {"id": image_id, "message": "Image processed successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))