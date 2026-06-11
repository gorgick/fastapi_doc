FROM python:3.8-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add postgresql-client build-base postgresql-dev

RUN apk update && apk add bash

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip --no-warn-script-location

RUN pip install -r requirements.txt --no-cache-dir --no-warn-script-location

COPY main-app .

RUN chmod +x prestart.sh

ENTRYPOINT ["./prestart.sh"]
CMD ["python", "gunicorn_main.py"]