from flask import Flask, render_template, jsonify
import requests


app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home_page():
    return render_template("HomePage.html")

@app.route("/eth")
def eth():
    # Make a GET request to the CoinDesk API
    eth_response = requests.get("https://api.coingecko.com/api/v3/coins/")

    # Extract the Ethereum price from the API response
    if eth_response.status_code == 200:
        eth_data = eth_response.json()
        eth_price = eth_data[1]["market_data"]["current_price"]["usd"]
        eth_price_h24 = eth_data[1]["market_data"]["high_24h"]["usd"]
        eth_price_l24 = eth_data[1]["market_data"]["low_24h"]["usd"]

    # Pass the Bitcoin price data to the template
    return render_template("eth.html", eth_price=eth_price, eth_price_h24=eth_price_h24, eth_price_l24=eth_price_l24)

@app.route("/btc")
def btc():
    # Make a GET request to the CoinDesk API
    btc_response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order_by=market_cap&per_page=1")
    
    # Extract the Bitcoin price from the API response
    if btc_response.status_code == 200:
        btc_data = btc_response.json()
        bitcoin_price = btc_data[0]["current_price"]
        bitcoin_price_h24 = btc_data[0]["high_24h"]
        bitcoin_price_l24 = btc_data[0]["low_24h"]


    # Pass the Bitcoin price data to the template
    return render_template("btc.html", bitcoin_price=bitcoin_price, bitcoin_price_h24=bitcoin_price_h24, bitcoin_price_l24=bitcoin_price_l24)



if __name__ == '__main__':
    app.run()
