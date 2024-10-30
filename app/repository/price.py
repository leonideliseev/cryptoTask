from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Price

from .repository import Repository


class PriceRepository(Repository):
    @staticmethod
    async def get_prices(
        session: AsyncSession,
        ticker: str,
    ) -> list[Price]:
        query = select(Price).where(Price.ticker == ticker)
        result: Result = await session.execute(query)
        prices = result.scalars().all()

        return list(prices)

    @staticmethod
    async def get_latest_price(
        session: AsyncSession,
        ticker: str,
    ) -> Price | None:
        query = (
            select(Price)
            .where(Price.ticker == ticker)
            .order_by(Price.timestamp.desc())
            .limit(1)
        )
        result: Result = await session.execute(query)
        price = result.scalar()

        return price

    @staticmethod
    async def get_prices_by_date(
        session: AsyncSession,
        ticker: str,
        start: int,
        end: int,
    ) -> list[Price]:
        query = select(Price).where(
            (Price.ticker == ticker)
            & (Price.timestamp >= start)
            & (Price.timestamp <= end)
        )
        result: Result = await session.execute(query)
        prices = result.scalars().all()

        return list(prices)
