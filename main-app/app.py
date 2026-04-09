from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router
from core import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    print("startup engine")
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dipose()


app = FastAPI(
    title="Websockets",
    description="/ws",
    lifespan=lifespan
)

app.include_router(router)
