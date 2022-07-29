from pathlib import Path

from loguru import logger
from singleton_decorator import singleton


@singleton
class FileManager:
    def __init__(self, path: str):
        path = Path(path)
        self.__parent = path if path.is_dir() else path.parent
        self.__siblings = [
            c for c in self.__parent.iterdir() if c.suffix in {".jpg", ".jpeg"}
        ]
        self.__file_path = self.__siblings[0] if path.is_dir() else path

    def file_browser_repr(self) -> str:
        returned = "Files |\n-|\n"
        for file in self.__siblings:
            if self.__file_path.name == file.name:
                returned += f"**{file.name}**\n"
            else:
                returned += f"{file.name}\n"
        return returned

    def get_current_image_file_path(self) -> str:
        logger.info(f"View file {self.__file_path}")
        return self.__file_path

    def right_file(self) -> None:
        logger.info("Select right file.")
        found = False
        for sibling in self.__siblings:
            if found:
                self.__file_path = sibling
                logger.info(f"New image file selected {self.__file_path}")
                break

            if sibling.name == self.__file_path.name:
                found = True

    def left_file(self) -> None:
        found = False
        for sibling in reversed(self.__siblings):
            if found:
                self.__file_path = sibling
                logger.info(f"New image file selected {self.__file_path}")
                break

            if sibling.name == self.__file_path.name:
                found = True
