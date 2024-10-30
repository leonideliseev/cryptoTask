import asyncio
from datetime import datetime

import aiohttp


class DeribitClient:
    BASE_URL = "https://www.deribit.com/api/v2/public"

    async def fetch_price(self, ticker: str) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.BASE_URL}/get_index_price", params={"index_name": ticker}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return {
                        "ticker": ticker,
                        "price": data["result"]["index_price"],
                        "timestamp": int(datetime.now().timestamp()),
                    }
                else:
                    raise Exception(f"Failed to fetch data: {response.status}")

    async def fetch_prices(self):
        tickers = ["btc_usd", "eth_usd"]
        tasks = [self.fetch_price(ticker) for ticker in tickers]
        return await asyncio.gather(*tasks)
