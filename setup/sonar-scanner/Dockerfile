FROM sonarsource/sonar-scanner-cli

COPY ./setup/postgres/docker-entrypoint-initdb.d/init-postgres.sh /docker-entrypoint-initdb.d/init-postgres.sh

COPY ./app /usr/src
COPY sonar-project.properties /usr/src/sonar-project.properties
COPY sonar-project.properties /opt/sonar-scanner/conf
CMD mv /opt/sonar-scanner/conf/sonar-project.properties /opt/sonar-scanner/conf/sonar-scanner.properties
