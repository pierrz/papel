db.createUser({
    user: 'apiuser',
    pwd: 'apiuserpwd',
    roles: [
        {
            role: 'readWrite',
            db: 'sourcedb'
        }
    ],
});

// creation tests
db = new Mongo().getDB('sourcedb');

db.createCollection('dev', { capped: false });
db.dev.insert([
    { "item": 1 },
    { "item": 2 },
    { "item": 3 },
    { "item": 4 },
    { "item": 5 }
]);
