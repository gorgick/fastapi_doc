import uvicorn as uvicorn
from fastapi import FastAPI

main_app = FastAPI()


@main_app.get("/")
async def root():
    return {"message": "hello"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
