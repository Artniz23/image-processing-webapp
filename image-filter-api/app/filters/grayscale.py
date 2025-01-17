from PIL import Image

class GrayscaleFilter:
    def apply(self, image: Image.Image) -> Image.Image:
        return image.convert("L")