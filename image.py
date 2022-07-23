import exif
import PIL
from loguru import logger

from models import ImageDescription, TagModel


class Image:
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name
        self.__image = PIL.Image.open(file_name)

        with open(file_name, "rb") as palm_1_file:
            self.__palm_1_image = exif.Image(palm_1_file)

    @property
    def pil_image(self) -> PIL.Image:
        return self.__image

    def add_image_description(self, image_description: ImageDescription):
        self.__palm_1_image.set("image_description", image_description.json())
        with open(self.__file_name, "wb") as image_file:
            image_file.write(self.__palm_1_image.get_file())

    def add_tag(self, new_tag: TagModel):
        current_description = self.__get_image_description()
        current_description.tags.append(new_tag)
        self.add_image_description(current_description)

    def __get_image_description(self) -> ImageDescription:
        try:
            return ImageDescription.parse_raw(
                str(self.__palm_1_image.image_description)
            )
        except Exception:
            return ImageDescription()

    def get_information(self) -> str:
        return f"# Information\n\n{self.__get_image_description().compact()}"
