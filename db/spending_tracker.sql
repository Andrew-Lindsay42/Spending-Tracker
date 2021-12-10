DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  budget DECIMAL,
  payday INT
);

CREATE TABLE merchants(
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  active BOOLEAN,
  icon_num INT
);

CREATE TABLE tags(
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  active BOOLEAN,
  icon_num INT
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    amount DECIMAL,
    transaction_date date,
    decription VARCHAR(255),
    merchant INT REFERENCES merchants(id),
    tag INT REFERENCES tags(id)
);

INSERT INTO users (name, budget, payday) VALUES ('user', 0, 1)