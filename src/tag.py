from models import FrameModel


class Tag:
    def __init__(self, name: str, frame: FrameModel) -> None:
        self.__name = name
        self.__frame = frame

    @property
    def name(self) -> str:
        return self.__name

    @property
    def frame(self) -> FrameModel:
        return self.__frame
