from app import create_app
from core.settings import settings
from gunicorn_app import GunicornApplication, get_app_options

main_app = create_app()


def main():
    app = GunicornApplication(
        app=main_app,
        options=get_app_options(
            host=settings.gunicorn.host,
            port=settings.gunicorn.port,
            timeout=settings.gunicorn.timeout,
            workers=settings.gunicorn.workers,
        ),
    )
    app.run()


if __name__ == "__main__":
    main()
