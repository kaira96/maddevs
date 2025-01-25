# Шаблон README
## Структура репозитория
1. `new_job/main/tests` = <Название папки с тестами>
2. `new_job/main` = <Название папки с кодом>
3. `new_job/docker-compose.yml` = <Название `dockerfile` или `docker-compose.yaml`>
4. `new_job/user/migrations` = <Название и путь до файлов миграций в БД>

- `python ^3.13`
- `poetry ==2.0.1`
- `django >=5.1.5,<6.0.0`
- `djangorestframework >=3.15.2,<4.0.0`
- `djangorestframework-simplejwt >=5.4.0,<6.0.0`
- `drf-spectacular >=0.28.0,<0.29.0`
- `postgres ^17.0,<18.0`

## Как запустить локальное окружение через docker
```sh
$ git clone 'link'
$ cp .env.sample .env
$ docker-compose -f docker-compose.yml up --build -d
$ docker-compose logs # For see containers logs.
```

## Как запустить локальное окружение через локальную машину
```sh
$ Configure Postgres DB (create db, user)
$ git clone 'link'
$ activate venv
$ pip install poetry
$ cd main
$ poetry install
$ pyhton manage.py migrate
$ pyhton manage.py createsuperuser
$ pyhton manage.py runserver
```
## Как выполнять тесты
```sh
$ pytest --cov
```