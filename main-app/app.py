from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router
from core import db_helper
from tables import Deribit


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dipose()


app = FastAPI(
    title="Websockets",
    description="/ws",
    lifespan=lifespan
)

app.include_router(router)
