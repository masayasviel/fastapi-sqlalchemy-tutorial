# fastapi-sqlalchemy-tutorial

## venv

```sh
make venv
```

## activate

```sh
source .venv/bin/activate
deactivate
```

## db

```shell
make up
```

### migrate

```sh
# init
docker-compose run web alembic init migrations
# create migration file
docker-compose run web alembic revision --autogenerate
# apply db
docker-compose run web alembic upgrade head
```

### php my admin

`http://localhost:8080`

## docker

```shell
make down
make down_volume
docker images -qa | xargs docker rmi
```

