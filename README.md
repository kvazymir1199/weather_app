![Header](git_hub/preview.png)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

# Weather Forecast

## Отписание

**«Weather Forecast»** - микросервис, который выводит данные о погоде в определенном городе.
Для проекта реализован сайт и апи.

### Функионал

1. Пользователь вводит в форму поиска город в котором нужно получить данные о погоде, запрос обрабатывается 
   и выводиться страница с данными.

2. При повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее.

3. Сохраняется история поиска

4. Для апи реализовано 2 эндпоинта: 1) Для получения списка городов и колличества запросов 
2) Данные для конкретного запрошенного города


# Технологии

- [Python 3.12](https://www.python.org/downloads/release/python-388/)
- [Django 4.2](https://www.djangoproject.com/download/)
- [Django Rest Framework 3.15.2](https://www.django-rest-framework.org/)
- [PostgreSQL 13.0](https://www.postgresql.org/download/)
- [gunicorn 22.0.0](https://pypi.org/project/gunicorn/)
- [nginx 1.27.0](https://nginx.org/ru/download.html)
- # Контейнер

- [Docker 20.10.14](https://www.docker.com/)
- [Docker Compose 2.4.1](https://docs.docker.com/compose/)

# URL's

- http://localhost/api/v1/
- http://localhost/weather

# Локальная установка

Клонируйте репозиторий и перейдите в него в командной строке:

```sh
git clone https://github.com/kvazymir1199/weather_app.git && cd weather_app_main
```

Создайте .env файл командой:

```sh
touch .env
```

и заполните его данными:

```sh
#.env
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных postgres>
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<секретный ключ проекта django>
```

Выполните команду

```sh
docker-compose up -d
```
Для начала работы с бд выполните миграции
```sh
docker-compose run backend python manage.py migrate
```
Для подключения CSS стилей выполните команду 

```sh
docker-compose run backend python manage.py collectstatic
```



Перейдите по ссылке и следуйте форме поиска

- http://localhost/weather

# Примеры запросов

**GET**: http://127.0.0.1:8000/api/users/
Пример ответа:

```json
[
  {
    "id": 1,
    "name": "Denis"
  },
  {
    "id": 2,
    "name": "Anton"
  },
  {
    "id": 3,
    "name": "Vladimir"
  },
  {
    "id": 4,
    "name": "Kiril"
  }
]
```

**GET**: http://127.0.0.1:8000/api/users/1/
Пример ответа:

```json
[
  {
    "id": 1,
    "name": "Denis"
  }
]
```

**GET**: http://127.0.0.1:8000/api/users/1/digest
Пример ответа:

```json
{
  "posts": [
    "Сенсация: биткоин достиг исторического минимума",
    "В ожидании выхода God of War 3",
    "Рецепт Домашние блинчики с начинкой",
    "Курс рубля показывает 'небывалый успех'"
  ]
}
```

Для фильтрации по рейтингу используйте query_params в запросе
**GET**: http://127.0.0.1:8000/api/users/1/digest?rating=9
Пример ответа:

```json
{
  "posts": [
    "Сенсация: биткоин достиг исторического минимума"
  ]
}
```

## Автор:

* [kvazymir1199](https://github.com/kvazymir1199)