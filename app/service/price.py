from sqlalchemy.ext.asyncio import AsyncSession

from repository import Repository

from .response_models import PriceOut
from .service import Service


class PriceService(Service):
    def __init__(self, repo: Repository):
        super().__init__(repo)

    async def get_prices(self, session: AsyncSession, ticker: str) -> list[PriceOut]:
        prices = await self.repo.get_prices(session, ticker)
        return [PriceOut.from_orm(price) for price in prices]

    async def get_latest_price(
        self,
        session: AsyncSession,
        ticker: str,
    ) -> PriceOut | None:
        price = await self.repo.get_latest_price(session, ticker)
        if price is None:
            return None
        return PriceOut.from_orm(price)

    async def get_prices_by_date(
        self,
        session: AsyncSession,
        ticker: str,
        start: int,
        end: int,
    ) -> list[PriceOut]:
        prices = await self.repo.get_prices_by_date(session, ticker, start, end)
        return [PriceOut.from_orm(price) for price in prices]
