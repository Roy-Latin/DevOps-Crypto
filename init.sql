CREATE DATABASE IF NOT EXISTS crypto;
USE crypto;

CREATE TABLE IF NOT EXISTS price_table (
  name VARCHAR(20),
  price FLOAT(10)
);

INSERT INTO price_table (name, price)
VALUES
  ('Ethereum', 1900.0)