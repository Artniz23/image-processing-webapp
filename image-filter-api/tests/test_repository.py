import pytest

from app.models.dtos import SaveImageDTO
from app.repositories.image_repository import ImageRepository

@pytest.fixture
def repository(mocker):
    mock_collection = mocker.Mock()
    repository = ImageRepository(mock_collection)

    return repository

def test_save_image(repository):
    """
    Тестирует сохранение изображения в базу данных.
    """
    save_image_dto = SaveImageDTO(
        filter_name="grayscale",
        original_image=b"original_data",
        processed_image=b"processed_data"
    )

    repository.save_image(save_image_dto)
    repository.collection.insert_one.assert_called_once_with(save_image_dto.model_dump())

def test_get_image_id(repository):
    """
    Тестирует получение изображения по id
    """

    image_id = "1"

    repository.get_image_by_id(image_id)

    repository.collection.find_one.assert_called_once_with({"_id": image_id})