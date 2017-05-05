CREATE TABLE language(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    japanese TEXT NOT NULL,
    english TEXT NOT NULL,
    chinese TEXT NOT NULL,
    lock BOOLEAN NOT NULL DEFAULT FALSE,
    add_timestamp TIMESTAMP WITHOUT TIME ZONE,
    update_timestamp TIMESTAMP WITHOUT TIME ZONE
);