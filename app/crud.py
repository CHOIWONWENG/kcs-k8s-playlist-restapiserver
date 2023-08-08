from sqlalchemy.sql import select
from .database import database
from .models import Playlist

async def create_playlist(playlist: Playlist):
    query = Playlist.__table__.insert().values(**playlist.dict())
    last_record_id = await database.execute(query)
    return {**playlist.dict(), "id": last_record_id}

async def get_playlist(playlist_id: int):
    query = select(Playlist).where(Playlist.id == playlist_id)
    result = await database.fetch_one(query)
    return result

async def update_playlist(playlist_id: int, new_playlist: Playlist):
    query = (
        Playlist.__table__
        .update()
        .where(Playlist.id == playlist_id)
        .values(title=new_playlist.title, description=new_playlist.description)
    )
    await database.execute(query)

async def delete_playlist(playlist_id: int):
    query = Playlist.__table__.delete().where(Playlist.id == playlist_id)
    await database.execute(query)