-- Create table
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL,
    username VARCHAR(64) UNIQUE,
    password_hash VARCHAR(64)
);

-- admin:admin
INSERT INTO users (username, password_hash)
VALUES (
        'admin',
        '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
    );