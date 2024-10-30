from database import engine
from price import Price


async def save_prices(prices: list):
    async with engine.get_session() as session:
        async with session.begin():
            for price_data in prices:
                price = Price(**price_data)
                session.add(price)
