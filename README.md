# django-ioio
Django Website

Rebuilding my website in Django.


## Run

### Dev Local

```
set -o allexport; source ../.env.dev; set +o allexport; ./manage.py runserve
```

### Dev Docker

```
docker-compose up
```

### Prod

```
docker-compose -f docker-compose.prod.yaml up
```


## Install

System requirements (for building psycopg)

```
sudo apt-get install postgresql libpq-dev python3-dev
```

Create a virtual environment:
```
python3 -m venv .venv
```

### Docker

```
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic --noinput
```