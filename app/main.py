from fastapi import FastAPI, HTTPException
from .crud import create_playlist, get_playlist, update_playlist, delete_playlist
from .models import Playlist
from .database import database
from sqlalchemy.sql import select

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await database.disconnect()

@app.post("/playlist/", response_model=Playlist)
async def post_playlist(playlist: Playlist):
    return await create_playlist(playlist)

@app.get("/playlist/{playlist_id}", response_model=Playlist)
async def read_playlist(playlist_id: int):
    playlist = await get_playlist(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist not found")
    return playlist

@app.put("/playlist/{playlist_id}", response_model=Playlist)
async def update_existing_playlist(playlist_id: int, new_playlist: Playlist):
    playlist = await get_playlist(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist not found")
    await update_playlist(playlist_id, new_playlist)
    return new_playlist

@app.delete("/playlist/{playlist_id}")
async def delete_existing_playlist(playlist_id: int):
    playlist = await get_playlist(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist not found")
    await delete_playlist(playlist_id)
    return {"message": "Playlist deleted successfully"}