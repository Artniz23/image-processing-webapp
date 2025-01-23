from app.filters.filter_factory import FilterFactory
from PIL import Image
import io

from app.models.dtos import SaveImageDTO


class ImageService:
    def __init__(self, repository):
        self.repository = repository

    def process_image(self, filter_name: str, image_file: bytes, content_type: str):
        # Открыть изображение
        image = Image.open(io.BytesIO(image_file))
        # Применить фильтр
        filter_class = FilterFactory.get_filter(filter_name)
        if not filter_class:
            raise ValueError("Invalid filter name")
        filtered_image = filter_class().apply(image)
        # Сохранить изображение
        output = io.BytesIO()
        filtered_image.save(output, format=self.get_pillow_format(content_type))
        output.seek(0)
        return output.getvalue()

    def save_processed_image(self, filter_name: str, original_image: bytes, processed_image: bytes):
        save_image_dto = SaveImageDTO(
            filter_name=filter_name,
            original_image=original_image,
            processed_image=processed_image
        )

        return self.repository.save_image(save_image_dto)

    # Функция для преобразования MIME-типа в формат Pillow
    def get_pillow_format(self, content_type: str) -> str:
        mime_to_format = {
            "image/jpeg": "JPEG",
            "image/png": "PNG",
            "image/gif": "GIF",
            "image/webp": "WEBP",
            "image/bmp": "BMP",
        }
        return mime_to_format.get(content_type, "JPEG")  # По умолчанию JPEG