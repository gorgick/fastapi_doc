from fastapi import FastAPI
from gunicorn.app.base import BaseApplication


def get_app_options(host: str, port: int, workers: int, timeout: int) -> dict:
    return {
        "accesslog": "-",
        "errorlog": "-",
        "bind": f"{host}:{port}",
        "workers": workers,
        "timeout": timeout,
        "worker_class": "uvicorn.workers.UvicornWorker"
    }


class GunicornApplication(BaseApplication):

    def __init__(self, app: FastAPI, options: dict):
        self.app = app
        self.options = options
        super().__init__()

    def load(self):
        return self.app

    @property
    def config_options(self) -> dict:
        return {
            k: v
            for k, v in self.options.items()
            if k in self.cfg.settings and v is not None
        }

    def load_config(self):
        for key, value in self.config_options.items():
            self.cfg.set(key.lower(), value)
