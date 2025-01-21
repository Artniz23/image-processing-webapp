from PIL import Image

class GrayscaleFilter:
    description = "Convert image to grayscale"

    def apply(self, image: Image.Image) -> Image.Image:
        return image.convert("L")