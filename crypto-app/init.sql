CREATE DATABASE IF NOT EXISTS crypto;
USE crypto;

CREATE TABLE IF NOT EXISTS eth_price_table (
  name VARCHAR(20),
  price FLOAT(10)
);

CREATE TABLE IF NOT EXISTS btc_price_table (
  name VARCHAR(20),
  price FLOAT(10)
);

CREATE TABLE IF NOT EXISTS xrp_price_table (
  name VARCHAR(20),
  price FLOAT(10)
);

CREATE TABLE IF NOT EXISTS ada_price_table (
  name VARCHAR(20),
  price FLOAT(10)
);