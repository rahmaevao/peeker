from pathlib import Path

from loguru import logger


class FileManager:
    def __init__(self, path: str):
        path = Path(path)
        self.__parent = path if path.is_dir() else path.parent
        self.__siblings = [c for c in self.__parent.iterdir() if c.suffix in {".jpg", ".jpeg"}]
        self.__file_path = path if not path.is_dir else self.__siblings[0]

        logger.info(f"{self.__parent=}, {self.__siblings=}, {self.__file_path=}")
    
    def file_browser_repr(self) -> str:
        returned = "Files |\n-|\n"
        for file in self.__siblings:
            if self.__file_path.name == file.name:
                returned += f"**{file.name}**\n"
            else:
                returned += f"{file.name}\n"

        logger.info(f"{returned=}")
        return returned
    
    def get_current_image_file_path(self) -> str:
        return self.__file_path

    def right_file(self):
        pass

    def left_file(self):
        pass
