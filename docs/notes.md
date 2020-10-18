# Django ioio

## Credit

Heavily based on https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#gunicorn

## Cheat Sheet

### Shell

```
docker ps
docker exec -it qwe123 bash
```

or:

```
docker-compose exec web bash
```

### DB

#### Backup

```
docker-compose exec db pg_dump --username=db_user --dbname=db_name > /tmp/ioio-pg.sql
```

#### Restore

Note the magical `-T` flag.

```
docker-compose exec -T db psql --username=db_user --dbname=db_name < /tmp/ioio-pg.sql
```