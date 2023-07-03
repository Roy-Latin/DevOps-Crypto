from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home_page():
    return render_template("HomePage.html")

@app.route("/eth")
def eth():
    # Make a GET request to the CoinGecko API
    eth_response = requests.get("https://api.coingecko.com/api/v3/coins/ethereum")

    # Extract the Ethereum price from the API response
    if eth_response.status_code == 200:
        eth_data = eth_response.json()
        eth_price = eth_data["market_data"]["current_price"]["usd"]
        eth_price_h24 = eth_data["market_data"]["high_24h"]["usd"]
        eth_price_l24 = eth_data["market_data"]["low_24h"]["usd"]

    # Pass the Ethereum price data to the template
    return render_template("eth.html", eth_price=eth_price, eth_price_h24=eth_price_h24, eth_price_l24=eth_price_l24)

@app.route("/btc")
def btc():
    # Make a GET request to the CoinDesk API
    btc_response = requests.get("https://api.coingecko.com/api/v3/coins/")
    
    # Extract the Bitcoin price from the API response
    if btc_response.status_code == 200:
        btc_data = btc_response.json()
        bitcoin_price = btc_data[0]["market_data"]["current_price"]["usd"]
        bitcoin_price_h24 = btc_data[0]["market_data"]["high_24h"]["usd"]
        bitcoin_price_l24 = btc_data[0]["market_data"]["low_24h"]["usd"]


    # Pass the Bitcoin price data to the template
    return render_template("btc.html", bitcoin_price=bitcoin_price, bitcoin_price_h24=bitcoin_price_h24, bitcoin_price_l24=bitcoin_price_l24)

@app.route("/xrp")
def xrp():
    # Make a GET request to the CoinDesk API
    xrp_response = requests.get("https://api.coingecko.com/api/v3/coins/")
    
    # Extract the xrp price from the API response
    if xrp_response.status_code == 200:
        xrp_data = xrp_response.json()
        xrp_price = xrp_data[5]["market_data"]["current_price"]["usd"]
        xrp_price_h24 = xrp_data[5]["market_data"]["high_24h"]["usd"]
        xrp_price_l24 = xrp_data[5]["market_data"]["low_24h"]["usd"]


    # Pass the xrp price data to the template
    return render_template("xrp.html", xrp_price=xrp_price, xrp_price_h24=xrp_price_h24, xrp_price_l24=xrp_price_l24)

@app.route("/ada")
def ada():
    # Make a GET request to the CoinDesk API
    ada_response = requests.get("https://api.coingecko.com/api/v3/coins/")
    
    # Extract the ada price from the API response
    if ada_response.status_code == 200:
        ada_data = ada_response.json()
        ada_price = ada_data[7]["market_data"]["current_price"]["usd"]
        ada_price_h24 = ada_data[7]["market_data"]["high_24h"]["usd"]
        ada_price_l24 = ada_data[7]["market_data"]["low_24h"]["usd"]


    # Pass the adan price data to the template
    return render_template("ada.html", ada_price=ada_price, ada_price_h24=ada_price_h24, ada_price_l24=ada_price_l24)

if __name__ == '__main__':
    app.run()
