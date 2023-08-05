from pydantic import Field
from datetime import datetime
from beanie import Document, PydanticObjectId

class Playlist(Document):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    title: str
    author: str
    genre: str
    createdAt: datetime
    motifiedAt: datetime

    class Settings:
        name = "playlist"