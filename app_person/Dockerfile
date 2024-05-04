#FROM python:3.10
#
## Выбор папки, в которой будет вестись работа
#WORKDIR /app_person
#
## Установка зависимостей проекта
#COPY ./requirements.txt /app_person/
#RUN pip install --no-cache-dir --upgrade -r /app_person/requirements.txt
#
## Перенос проекта в образ
#COPY ./app /app_person/app
#COPY .env /app_person
#
## Копирование файлов alembic
#COPY ./migration /app_person/migration
#COPY ./alembic.ini /app_person/alembic.ini
#
#EXPOSE 8080
#
## Добавляем путь к корневому каталогу проекта в PYTHONPATH
#ENV PYTHONPATH="${PYTHONPATH}:/app_person"
#ENV PYTHONPATH="${PYTHONPATH}:/app_person/app"
#
#CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8080"]

FROM python:3.10

WORKDIR /app_person

# Установка зависимостей проекта
COPY ./requirements.txt /app_person/
RUN pip install --no-cache-dir --upgrade -r /app_person/requirements.txt

# Перенос проекта в образx
COPY ./app /app_person/app
COPY .env /app_person

# Копирование файлов alembic
COPY ./migration /app_person/migration
COPY ./alembic.ini /app_person/alembic.ini

EXPOSE  8080

# Добавляем путь к корневому каталогу проекта в PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app_person"
ENV PYTHONPATH="${PYTHONPATH}:/app_person/app"

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host  0.0.0.0 --port  8080"]