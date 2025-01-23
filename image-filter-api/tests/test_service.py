import pytest
from app.services.image_service import ImageService
from pathlib import Path

@pytest.fixture
def service(mocker):
    mock_repo = mocker.Mock()
    return ImageService(mock_repo)

def test_process_image(service):
    """
    Тестирует корректную обработку изображения.
    """

    base_path = Path(__file__).parent
    file_path = base_path / "images" / "test_image.jpeg"

    with open(file_path, "rb") as file:
        image = file.read()
    processed_image = service.process_image("grayscale", image)
    assert processed_image is not None
    assert isinstance(processed_image, bytes)

def test_process_image_with_invalid_filter_name(service):
    """
    Тестирует выброшенную ошибку из-за неправильного названия фильтра.
    """

    base_path = Path(__file__).parent
    file_path = base_path / "images" / "test_image.jpeg"

    with open(file_path, "rb") as file:
        image = file.read()
    with pytest.raises(ValueError):
        service.process_image("not_valid_filter", image)

def test_save_processed_image(service):
    """
    Тестирует сохранение обработанного изображения.
    """

    original_image = b"original_image_data"
    processed_image = b"processed_image_data"

    image_id = service.save_processed_image("grayscale", original_image, processed_image)

    service.repository.save_image.assert_called_once()
    assert image_id is not None