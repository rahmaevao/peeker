from loguru import logger

from models import FrameModel, TagModel


class Tag:
    def __init__(self, name: str, frame: FrameModel) -> None:
        self.__name = name
        self.__frame = frame

        logger.info(f"{name, frame}")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def frame(self) -> FrameModel:
        return self.__frame
