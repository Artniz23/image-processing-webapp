from PIL import Image


class SepiaFilter:
    def apply(self, image: Image.Image) -> Image.Image:
        # Преобразуем изображение в черно-белое
        grayscale = image.convert("L")

        # Преобразуем обратно в RGB
        sepia_image = Image.new("RGB", grayscale.size)
        pixels = grayscale.load()  # Пиксели черно-белого изображения
        sepia_pixels = sepia_image.load()  # Пиксели сепия-изображения

        for y in range(grayscale.height):
            for x in range(grayscale.width):
                gray = pixels[x, y]
                r = int(gray * 240 / 255)  # Усиление красного
                g = int(gray * 200 / 255)  # Усиление зеленого
                b = int(gray * 145 / 255)  # Усиление синего
                sepia_pixels[x, y] = (r, g, b)

        return sepia_image