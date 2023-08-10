from flask import Flask, render_template, jsonify
import requests
import mysql.connector
import time

app = Flask(__name__, static_url_path='/static')

def create_database():
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'mysql-service',  # Use the service name as the hostname
        'database': 'crypto',
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Create the 'crypto' database
    cursor.execute('CREATE DATABASE IF NOT EXISTS crypto')

    # Switch to the 'crypto' database
    cursor.execute('USE crypto')

    # Create the 'eth_price_table' table
    cursor.execute('CREATE TABLE IF NOT EXISTS eth_price_table (name VARCHAR(20), price FLOAT(10))')

    # Create the 'btc_price_table' table
    cursor.execute('CREATE TABLE IF NOT EXISTS btc_price_table (name VARCHAR(20), price FLOAT(10))')

    # Create the 'xrp_price_table' table
    cursor.execute('CREATE TABLE IF NOT EXISTS xrp_price_table (name VARCHAR(20), price FLOAT(10))')

    # Create the 'ada_price_table' table
    cursor.execute('CREATE TABLE IF NOT EXISTS ada_price_table (name VARCHAR(20), price FLOAT(10))')

    connection.commit()
    cursor.close()
    connection.close()

def eth_price_table(name: str, price: float) -> None:
    config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-service',  # Use the service name as the hostname
    'database': 'crypto',
}
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Insert the name and price into the price_table
    cursor.execute('INSERT INTO eth_price_table (name, price) VALUES (%s, %s)', (name, price))

    # Commit the changes to the database
    connection.commit()

    cursor.close()
    connection.close()

def btc_price_table(name: str, price: float) -> None:
    config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-service',  # Use the service name as the hostname
    'database': 'crypto',
}
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Insert the name and price into the price_table
    cursor.execute('INSERT INTO btc_price_table (name, price) VALUES (%s, %s)', (name, price))

    # Commit the changes to the database
    connection.commit()

    cursor.close()
    connection.close()

def xrp_price_table(name: str, price: float) -> None:
    config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-service',  # Use the service name as the hostname
    'database': 'crypto',
}
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Insert the name and price into the price_table
    cursor.execute('INSERT INTO xrp_price_table (name, price) VALUES (%s, %s)', (name, price))

    # Commit the changes to the database
    connection.commit()

    cursor.close()
    connection.close()

def ada_price_table(name: str, price: float) -> None:
    config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-service',  # Use the service name as the hostname
    'database': 'crypto',
}
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Insert the name and price into the price_table
    cursor.execute('INSERT INTO ada_price_table (name, price) VALUES (%s, %s)', (name, price))

    # Commit the changes to the database
    connection.commit()

    cursor.close()
    connection.close()

@app.route("/")
def home_page():
    return render_template("HomePage.html")

@app.route("/eth")
def eth():
    # Make a GET request to the CoinGecko API
    eth_response = requests.get("https://api.coingecko.com/api/v3/coins/ethereum")

    # Add a delay of 3 seconds
    time.sleep(3)

    # Extract the Ethereum price from the API response
    if eth_response.status_code == 200:
        eth_data = eth_response.json()
        eth_price = eth_data["market_data"]["current_price"]["usd"]
        eth_price_h24 = eth_data["market_data"]["high_24h"]["usd"]
        eth_price_l24 = eth_data["market_data"]["low_24h"]["usd"]

    # Update the price_table with the Ethereum price data
    eth_price_table("Ethereum", eth_price)
    
    config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-service',  # Use the service name as the hostname
    'database': 'crypto',
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Fetch the data from the eth_price_table
    cursor.execute('SELECT name, price FROM eth_price_table')
    eth_price_data = cursor.fetchall()

    cursor.close()
    connection.close()

    # Pass the Ethereum price data to the template
    return render_template("eth.html", eth_price=eth_price, eth_price_h24=eth_price_h24, eth_price_l24=eth_price_l24,eth_price_data=eth_price_data )

@app.route("/btc")
def btc():
    # Make a GET request to the CoinDesk API
    btc_response = requests.get("https://api.coingecko.com/api/v3/coins/")

    # Add a delay of 3 seconds
    time.sleep(3)
    
    # Extract the Bitcoin price from the API response
    if btc_response.status_code == 200:
        btc_data = btc_response.json()
        bitcoin_price = btc_data[0]["market_data"]["current_price"]["usd"]
        bitcoin_price_h24 = btc_data[0]["market_data"]["high_24h"]["usd"]
        bitcoin_price_l24 = btc_data[0]["market_data"]["low_24h"]["usd"]

    # Update the price_table with the Ethereum price data
    btc_price_table("Bitcoin", bitcoin_price)
    
    config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-service',  # Use the service name as the hostname
    'database': 'crypto',
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Fetch the data from the eth_price_table
    cursor.execute('SELECT name, price FROM btc_price_table')
    btc_price_data = cursor.fetchall()

    cursor.close()
    connection.close()

    # Pass the Bitcoin price data to the template
    return render_template("btc.html", bitcoin_price=bitcoin_price, bitcoin_price_h24=bitcoin_price_h24, bitcoin_price_l24=bitcoin_price_l24, btc_price_data=btc_price_data)

@app.route("/xrp")
def xrp():
    # Make a GET request to the CoinDesk API
    xrp_response = requests.get("https://api.coingecko.com/api/v3/coins/")

    # Add a delay of 3 seconds
    time.sleep(3)
    
    # Extract the xrp price from the API response
    if xrp_response.status_code == 200:
        xrp_data = xrp_response.json()
        xrp_price = xrp_data[5]["market_data"]["current_price"]["usd"]
        xrp_price_h24 = xrp_data[5]["market_data"]["high_24h"]["usd"]
        xrp_price_l24 = xrp_data[5]["market_data"]["low_24h"]["usd"]

    # Update the price_table with the Ethereum price data
    xrp_price_table("Ripple", xrp_price)

    config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-service',  # Use the service name as the hostname
    'database': 'crypto',
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Fetch the data from the eth_price_table
    cursor.execute('SELECT name, price FROM xrp_price_table')
    xrp_price_data = cursor.fetchall()

    cursor.close()
    connection.close()

    # Pass the xrp price data to the template
    return render_template("xrp.html", xrp_price=xrp_price, xrp_price_h24=xrp_price_h24, xrp_price_l24=xrp_price_l24, xrp_price_data=xrp_price_data)

@app.route("/ada")
def ada():
    # Make a GET request to the CoinDesk API
    ada_response = requests.get("https://api.coingecko.com/api/v3/coins/")

    # Add a delay of 3 seconds
    time.sleep(3)
    
    # Extract the ada price from the API response
    if ada_response.status_code == 200:
        ada_data = ada_response.json()
        ada_price = ada_data[7]["market_data"]["current_price"]["usd"]
        ada_price_h24 = ada_data[7]["market_data"]["high_24h"]["usd"]
        ada_price_l24 = ada_data[7]["market_data"]["low_24h"]["usd"]

    # Update the price_table with the Ethereum price data
    ada_price_table("Cardano", ada_price)

    config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql-service',  # Use the service name as the hostname
    'database': 'crypto',
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Fetch the data from the eth_price_table
    cursor.execute('SELECT name, price FROM ada_price_table')
    ada_price_data = cursor.fetchall()

    cursor.close()
    connection.close()

    # Pass the adan price data to the template
    return render_template("ada.html", ada_price=ada_price, ada_price_h24=ada_price_h24, ada_price_l24=ada_price_l24, ada_price_data=ada_price_data)

if __name__ == '__main__':
    create_database()
    app.run(host='0.0.0.0')