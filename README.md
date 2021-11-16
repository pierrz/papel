# papel
<br>

A boilerplate docker based repository, embedded with
- FastAPI
- Celery + Rabbit-MQ + Flower
- Postgres + PGAdmin

<br>

#### Installation
You should use the `main` branch, other branches being used for development purpose.
You might have to mount your certificate in the nginx container volume such as what is done here :
```
volumes:
    - /etc/letsencrypt:/etc/letsencrypt:ro
```
And also create the related `certificate.json` file.

Then you're left with creating the `.env` environment file, and `servers.json` if you use the `pgadmin` container.
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
