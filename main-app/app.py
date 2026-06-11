from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router
from core import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dipose()


app = FastAPI(
    title="Websockets",
    description="/ws",
    lifespan=lifespan
)


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
    )
    return app


app.include_router(router)
main_app = create_app()
main_app.include_router(router)
