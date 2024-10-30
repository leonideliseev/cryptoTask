import asyncio

from client import DeribitClient
from store_data import save_prices


async def main():
    client = DeribitClient()
    while True:
        prices = await client.fetch_prices()
        await save_prices(prices)
        await asyncio.sleep(60)  # Запуск каждую минуту


if __name__ == "__main__":
    asyncio.run(main())
