#!/usr/bin/bash -xe
curl -s '$1':5000
curl -s '$1':5000 | grep Crypto
curl -s '$1':5000/eth
curl -s '$1':5000/btc
curl -s '$1':5000/ada
curl -s '$1':5000/xrp
