#!/bin/bash
# Cf. https://hub.docker.com/_/postgres/

set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE "$DEV_DB";
    CREATE USER "$DEV_DB_USER";
    GRANT ALL PRIVILEGES ON DATABASE "$DEV_DB" TO "$DEV_DB_USER";
EOSQL
