#!/usr/bin/bash -xe
curl -s 192.168.56.1
curl -s 192.168.56.1 | grep Crypto
curl -s 192.168.56.1/eth | grep $
curl -s 192.168.56.1/btc | grep $
curl -s 192.168.56.1/ada | grep $
curl -s 192.168.56.1/xrp | grep $
