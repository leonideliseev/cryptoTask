import uvicorn
from fastapi import FastAPI

from endpoints import Endpoints, PriceEndpoints
from repository import PriceRepository, Repository
from service import PriceService, Service


def create_app() -> FastAPI:
    application = FastAPI()

    repository: Repository = PriceRepository()
    service: Service = PriceService(repository)
    endpoints: Endpoints = PriceEndpoints(service)
    application.include_router(endpoints.api_router)

    return application


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
