from PIL import ImageFilter, Image

class BlurFilter:
    def apply(self, image: Image.Image) -> Image.Image:
        # Применяем размытие
        return image.filter(ImageFilter.GaussianBlur(radius=5))