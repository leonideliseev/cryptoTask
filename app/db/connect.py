import os
from asyncio import current_task
from typing import AsyncIterator

from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)


class Settings(BaseSettings):
    user: str = str(os.getenv("DB_USER", "postgres"))
    password: str = str(os.getenv("DB_PASSWORD"))
    host: str = str(os.getenv("DB_HOST", "db"))
    port: str = str(os.getenv("DB_PORT", "5432"))
    name: str = str(os.getenv("DB_NAME", "prices"))
    db_echo: bool = bool(os.getenv("DB_ECHO", True))

    def get_db_url(self) -> str:
        row = (
            f"postgresql+asyncpg://{self.user}:"
            f"{self.password}@{self.host}:"
            f"{self.port}/{self.name}"
        )
        return row


settings = Settings()


class Engine:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )

        return session

    async def get_session(self) -> AsyncIterator[AsyncSession]:
        session = self.get_scoped_session()
        yield session
        await session.close()


engine = Engine(url=settings.get_db_url(), echo=settings.db_echo)
