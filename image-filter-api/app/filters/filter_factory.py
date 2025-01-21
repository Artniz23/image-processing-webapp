from app.filters.grayscale import GrayscaleFilter
from app.filters.sepia import SepiaFilter
from app.filters.blur import BlurFilter


class FilterFactory:
    filters = {
        "grayscale": GrayscaleFilter,
        "sepia": SepiaFilter,
        "blur": BlurFilter,
    }

    @classmethod
    def get_filters(cls):
        return [
            {"name": filter_name, "description": filter_class.description}
            for filter_name, filter_class in cls.filters.items()
        ]

    @classmethod
    def get_filter(cls, filter_name: str):
        return cls.filters.get(filter_name)
