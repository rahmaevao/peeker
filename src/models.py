from pydantic import BaseModel


class TagModel(BaseModel):
    name: str
    id: str = ""
    x: float
    y: float
    w: float
    h: float


class ImageDescription(BaseModel):
    description: str = (
        "Tags for Peeker software. Contact `rahmaevao@gmail.com` for details"
    )
    version: str = "0.1.0"
    tags: list[TagModel] = []

    def compact(self) -> str:
        return str(self.tags)


class FrameModel(BaseModel):
    left: int
    top: int
    width: int
    height: int
