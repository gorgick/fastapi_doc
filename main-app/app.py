from fastapi import FastAPI

from api import router


app = FastAPI(
    title="Websockets",
    description="/ws",
)

app.include_router(router)
