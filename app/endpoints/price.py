from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db import engine
from service import Service
from service.response_models import PriceOut

from .endpoints import Endpoints


class PriceEndpoints(Endpoints):
    def __init__(self, serv: Service):
        super().__init__(serv)

        self.api_router.add_api_route(
            "/", self.get_prices, methods=["GET"], status_code=200
        )
        self.api_router.add_api_route(
            "/latest/", self.get_latest_price, methods=["GET"], status_code=200
        )
        self.api_router.add_api_route(
            "/by_date/", self.get_prices_by_date, methods=["GET"], status_code=200
        )

    async def get_prices(
        self,
        ticker: str,
        session: AsyncSession = Depends(engine.get_session),
    ) -> List[PriceOut]:
        return await self.serv.get_prices(session, ticker)

    async def get_latest_price(
        self,
        ticker: str,
        session: AsyncSession = Depends(engine.get_session),
    ) -> PriceOut:
        price = await self.serv.get_latest_price(session, ticker)
        if price is None:
            raise HTTPException(
                status_code=404, detail=f"Price for ticker '{ticker}' not found."
            )
        return price

    async def get_prices_by_date(
        self,
        ticker: str,
        start: int,
        end: int,
        session: AsyncSession = Depends(engine.get_session),
    ) -> List[PriceOut]:
        return await self.serv.get_prices_by_date(session, ticker, start, end)
