from fastapi import APIRouter, HTTPException, status, Request, Form
from beanie import PydanticObjectId
from database.connection import Database
from models.playlist import Playlist
from datetime import datetime

router = APIRouter(
    tags = ['playlist']
)

playlist_database = Database(Playlist)

@router.get('/', status_code=status.HTTP_200_OK)
async def getPlaylist():
    playlist = await playlist_database.get_all()
    return playlist

@router.get('/{play_id}', status_code=status.HTTP_200_OK)
async def getPlay(play_id: PydanticObjectId):
    play = await playlist_database.get(play_id)
    return play

@router.post('/', status_code=status.HTTP_201_CREATED)
async def insertPlay( title: str = Form(...),
    writer: str = Form(...),
    genre: str = Form(...)):
    play = Playlist(title=title, writer=writer, genre=genre)
    play.createdAt = datetime.now()
    play.motifiedAt = datetime.now()
    await playlist_database.save(play)
    return play

@router.put('/{play_id}', status_code=status.HTTP_200_OK)
async def updatePlay(play_id: PydanticObjectId, title: str = Form(...), writer: str = Form(...), genre: str = Form(...)):
    existing_play = await playlist_database.get(play_id)
    if existing_play is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist not found")
    
    existing_play.title = title
    existing_play.writer = writer
    existing_play.genre = genre
    existing_play.motifiedAt = datetime.now()
    
    await playlist_database.save(existing_play)
    return existing_play

@router.delete('/{play_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_ota(play_id: PydanticObjectId):
    success = await playlist_database.delete(play_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return None
