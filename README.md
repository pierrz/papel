# papel

<br>A boilerplate docker based repository, embedded with 
- FastAPI
- Celery + Rabbit-MQ + Flower
- Postgres + PGAdmin


#### Installation
`docker-compose up`

You might have to mount your certificate in the nginx container volume such as :
```
volumes:
    - /etc/letsencrypt:/etc/letsencrypt:ro
```

   
#### [backlog]
 - (massive) dummy json data generator/sources
 - ported to Mongo via Spark
 - exposed via FastApi and GraphQL
 - crawled via Airflow and loaded into Elastic Search
 - exploratory frontend with Vue.js
