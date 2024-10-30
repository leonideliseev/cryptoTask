from abc import abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from repository import Repository

from .response_models import PriceOut


class Service:
    def __init__(self, repo: Repository):
        self.repo = repo

    @abstractmethod
    async def get_prices(self, session: AsyncSession, ticker: str) -> list[PriceOut]:
        pass

    @abstractmethod
    async def get_latest_price(
        self,
        session: AsyncSession,
        ticker: str,
    ) -> PriceOut | None:
        pass

    @abstractmethod
    async def get_prices_by_date(
        self,
        session: AsyncSession,
        ticker: str,
        start: int,
        end: int,
    ) -> list[PriceOut]:
        pass
