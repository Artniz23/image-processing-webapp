from PIL import ImageFilter, Image

class BlurFilter:
    description = "Blur the image"

    def apply(self, image: Image.Image) -> Image.Image:
        # Применяем размытие
        return image.filter(ImageFilter.GaussianBlur(radius=5))