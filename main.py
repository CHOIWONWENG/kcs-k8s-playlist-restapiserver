from fastapi import FastAPI
from routers import playlist
from database.connection import Settings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
settings = Settings()
app.include_router(playlist.router, prefix='/playlist')

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def init_db():
    await settings.initialize_database()
