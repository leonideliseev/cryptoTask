from abc import ABC, abstractmethod
from typing import List

from fastapi import APIRouter

from service import Service
from service.response_models import PriceOut


class Endpoints(ABC):
    def __init__(self, serv: Service):
        self.serv = serv
        self.api_router = APIRouter(prefix="/prices", tags=["Price API"])

    @abstractmethod
    async def get_prices(self, ticker: str) -> List[PriceOut]:
        """Получение списка цен по тикеру"""
        pass

    @abstractmethod
    async def get_latest_price(self, ticker: str) -> PriceOut:
        """Получение последней цены по тикеру"""
        pass

    @abstractmethod
    async def get_prices_by_date(
        self, ticker: str, start: int, end: int
    ) -> List[PriceOut]:
        """Получение списка цен по тикеру за указанный диапазон дат"""
        pass
