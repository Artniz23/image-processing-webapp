from fastapi import APIRouter, UploadFile, HTTPException, File, Form
from fastapi.responses import StreamingResponse

from app.filters.filter_factory import FilterFactory
from app.models.dtos import ProcessImageResponseDTO
from app.services.image_service import ImageService
from app.repositories.image_repository import ImageRepository
import io

router = APIRouter()
repository = ImageRepository()
service = ImageService(repository)

@router.get("/filters")
async def get_filters():
    filters = FilterFactory.get_filters()
    return filters

@router.post("/process")
async def process_image(filter_name: str = Form(...), file: UploadFile = File(...)):
    try:
        original_image = await file.read()
        processed_image = service.process_image(filter_name, original_image)
        return StreamingResponse(io.BytesIO(processed_image), media_type="image/jpeg")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/save")
async def save_image(
        filter_name: str = Form(...),
        original_image_file: UploadFile = File(...),
        processed_image_file: UploadFile = File(...)
):
    try:
        original_image = await original_image_file.read()
        processed_image = await processed_image_file.read()

        image_id = service.save_processed_image(filter_name, original_image, processed_image)

        process_image_response_dto = ProcessImageResponseDTO(
            id=image_id,
            message="Изображение создано успешно",
        )

        return process_image_response_dto.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))