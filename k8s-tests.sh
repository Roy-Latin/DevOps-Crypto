#!/usr/bin/bash -xe

# Set the timeout value (in seconds)
timeout=10

# Make curl requests with a timeout
curl -s --max-time $timeout 192.168.56.1
curl -s --max-time $timeout 192.168.56.1 | grep Crypto
curl -s --max-time $timeout 192.168.56.1/eth | grep Price
curl -s --max-time $timeout 192.168.56.1/btc | grep Price
curl -s --max-time $timeout 192.168.56.1/ada | grep Price
curl -s --max-time $timeout 192.168.56.1/xrp | grep Price
