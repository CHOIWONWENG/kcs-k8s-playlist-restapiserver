from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId 
from models.playlist import Playlist
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
import os

# 환경변수로 DataBase URL을 가져오자. => 파일 말고!
class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    DATABASE_NAME: Optional[str] = "playlistdb"

    # 수정이 필요함
    async def initialize_database(self):
        # DB를 더 디테일하게 잡았다 분명히
        client = AsyncIOMotorClient(os.environ('PLAYLISTDBURL'))  # 환경 변수 선언 필요
        # client = AsyncIOMotorClient(self.DATABASE_URL) # .env 파일 필요
        await init_beanie(database=client[self.DATABASE_NAME], document_models=[Playlist])

    # class Config:
    #     env_file = ".env"

class Database:
    def __init__(self, model):
        self.model = model

    # 생성처리(레코드 하나[문서의 인스턴스]를 데이터베이스 컬렉션에 추가한다
    async def save(self, document: Any) -> None:
        await document.create()
        return None
    
    # 조회 처리(get_all은 인수가 없고 컬렉션의모든 레코드를 불러온다)
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True    