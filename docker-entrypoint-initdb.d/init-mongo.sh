#!/bin/bash
set -e

mongo --eval "db.createUser({
    user: '$MONGO_API_USER',
    pwd: '$MONGO_API_PWD',
    roles: [
        {
            role: 'readWrite',
            db: '$MONGO_INITDB_DATABASE'
        }
    ]
});

# creation tests
db = new Mongo().getDB('$MONGO_INITDB_DATABASE');

db.createCollection('dev', { capped: false });
db.dev.insert([
    { "item": 1 },
    { "item": 2 },
    { "item": 3 },
    { "item": 4 },
    { "item": 5 }
]);"
