import uvicorn
import settings

if __name__ == '__main__':
    uvicorn.run("main.app:app",
                host=settings.host,
                port=settings.port,
                reload=True)
