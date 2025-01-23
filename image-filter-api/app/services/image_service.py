from app.filters.filter_factory import FilterFactory
from PIL import Image
import io

from app.models.dtos import SaveImageDTO


class ImageService:
    def __init__(self, repository):
        self.repository = repository

    def process_image(self, filter_name: str, image_file: bytes):
        # Открыть изображение
        image = Image.open(io.BytesIO(image_file))

        # Применить фильтр
        filter_class = FilterFactory.get_filter(filter_name)
        if not filter_class:
            raise ValueError("Invalid filter name")

        filtered_image = filter_class().apply(image)

        # Сохранить изображение
        output = io.BytesIO()
        # TODO Сделать адаптивный format
        filtered_image.save(output, format="JPEG")
        output.seek(0)

        return output.getvalue()

    def save_processed_image(self, filter_name: str, original_image: bytes, processed_image: bytes):
        save_image_dto = SaveImageDTO(
            filter_name=filter_name,
            original_image=original_image,
            processed_image=processed_image
        )

        return self.repository.save_image(save_image_dto)