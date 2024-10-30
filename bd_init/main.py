import os
from typing import Any

from dotenv import load_dotenv
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

load_dotenv()


class Settings:
    user: str = os.getenv("DB_USER", "postgres")
    password: str = os.getenv("DB_PASSWORD", "password")
    host: str = os.getenv("DB_HOST", "localhost")
    port: str = os.getenv("DB_PORT", "5432")
    name: str = os.getenv("DB_NAME", "crypto_db")
    db_echo: bool = os.getenv("DB_ECHO", "True").lower() == "true"

    @property
    def db_url(self) -> str:
        row = (
            f"postgresql://{self.user}:"
            f"{self.password}@{self.host}:"
            f"{self.port}/{self.name}"
        )
        return row


settings = Settings()
Base: Any = declarative_base()


class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(Integer)


DATABASE_URL = settings.db_url
engine = create_engine(DATABASE_URL)


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
