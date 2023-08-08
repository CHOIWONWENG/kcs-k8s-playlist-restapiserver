from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Playlist(Base):
    __tablename__ = "playlist"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String)
    genre = Column(String)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    modifiedAt = Column(DateTime(timezone=True), onupdate=func.now())