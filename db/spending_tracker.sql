DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  budget DECIMAL DEFAULT 0,
  payday INT DEFAULT 1
);

CREATE TABLE merchants(
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  active BOOLEAN,
  icon_num INT DEFAULT 0
);

CREATE TABLE tags(
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  active BOOLEAN,
  icon_num INT DEFAULT 0
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    amount DECIMAL,
    transaction_date DATE,
    description VARCHAR(255) DEFAULT Null,
    merchant INT REFERENCES merchants(id) ON DELETE SET DEFAULT DEFAULT Null,
    tag INT REFERENCES tags(id) ON DELETE SET DEFAULT DEFAULT Null
);

INSERT INTO users (name) VALUES ('user');