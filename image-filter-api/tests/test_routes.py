import pytest
from fastapi.testclient import TestClient
from fastapi import status

from app.main import app
import io

@pytest.fixture
def client():
    return TestClient(app)

# Тест для маршрута /filters
def test_get_filters(client, mocker):
    mock_filters = ["grayscale", "sepia", "blur"]
    mock_get_filters = mocker.patch(
        "app.filters.filter_factory.FilterFactory.get_filters",
        return_value=mock_filters
    )

    response = client.get("/api/filters")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mock_filters
    mock_get_filters.assert_called_once()


# Тест для маршрута /process
def test_process_image(client, mocker):
    fake_image = b"fake_image_data"
    fake_processed_image = b"fake_processed_image"
    mime_type = "image/jpeg"
    filter_name = "grayscale"

    # Делаем мок метода process_image в сервисе
    mock_service = mocker.patch("app.services.image_service.ImageService.process_image", return_value=fake_processed_image)

    # Создаём фиктивный файл
    fake_file = io.BytesIO(fake_image)
    fake_file.name = "test.jpg"

    response = client.post(
        "/api/process",
        files={
            "file": (fake_file.name, fake_file, mime_type),
        },
        data={"filter_name": filter_name}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.content == fake_processed_image
    assert response.headers["content-type"] == mime_type
    mock_service.assert_called_once_with(filter_name, fake_image)


# Тест для маршрута /save
def test_save_image(client, mocker):
    fake_image_id = "fake_image_id"
    fake_image = b"fake_original_image"
    fake_processed_image = b"fake_processed_image"

    # Делаем мок метода save_processed_image в сервисе
    mock_service = mocker.patch(
        "app.services.image_service.ImageService.save_processed_image",
        return_value=fake_image_id
    )

    # Создаём фиктивные файлы
    original_file = io.BytesIO(fake_image)
    original_file.name = "original.jpg"

    processed_file = io.BytesIO(fake_processed_image)
    processed_file.name = "processed.jpg"

    response = client.post(
        "/api/save",
        files={
            "original_image_file": (original_file.name, original_file, "image/jpeg"),
            "processed_image_file": (processed_file.name, processed_file, "image/jpeg"),
        },
        data={"filter_name": "sepia"}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": fake_image_id,
        "message": "Изображение создано успешно"
    }
    mock_service.assert_called_once_with("sepia", fake_image, fake_processed_image)