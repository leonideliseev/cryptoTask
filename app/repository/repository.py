from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Price


class Repository(ABC):
    @staticmethod
    @abstractmethod
    async def get_prices(
        session: AsyncSession,
        ticker: str,
    ) -> list[Price]:
        pass

    @staticmethod
    @abstractmethod
    async def get_latest_price(
        session: AsyncSession,
        ticker: str,
    ) -> Price | None:
        pass

    @staticmethod
    @abstractmethod
    async def get_prices_by_date(
        session: AsyncSession,
        ticker: str,
        start: int,
        end: int,
    ) -> list[Price]:
        pass
