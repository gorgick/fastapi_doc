import uvicorn as uvicorn
from fastapi import FastAPI

main_app = FastAPI()


@main_app.get("/")
async def root():
    return {"message": "hello"}


if __name__ == '__main__':
    uvicorn.run("main:main_app",
                host=settings.host,
                port=settings.port,
                reload=True)
