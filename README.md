# papel
<br>

A boilerplate docker based repository, embedded with
- FastAPI
- Celery + Rabbit-MQ + Flower
- Postgres + PGAdmin

<br>

#### Installation
You might have to mount your certificate in the nginx container volume such as what is done here :
```
volumes:
    - /etc/letsencrypt:/etc/letsencrypt:ro
```
<br>

#### Run
Only the core containers
```
docker-compose docker-compose.yml up
```

\+ monitoring containers
```
docker-compose -f docker-compose.yml -f docker-compose.monitoring.yml up
```

\+ dummy app (including test container)
```
docker-compose -f docker-compose.yml -f docker-compose.monitoring.yml -f docker-compose.app.yml up
```
<br>

Docker is great but sometimes tricky ... when changes are made, don't forget to:
- Use the `--build` flag.
- Cleanse the database properly by using the `prune` and `rm` tools to purge volumes and containers.

<br>


#### Development
If you want to make some changes in this repo while following the same environment tooling.
```
poetry config virtualenvs.in-project true
poetry install && poetry shell
pre-commit install
```
