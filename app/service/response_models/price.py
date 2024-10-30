from pydantic import BaseModel


class PriceOut(BaseModel):
    id: int
    ticker: str
    price: float
    timestamp: int

    class Config:
        from_attributes = True
