#!/usr/bin/bash -xe
curl -s $EC2_IP_TEST:5000
curl -s $EC2_IP_TEST:5000 | grep Crypto
curl -s $EC2_IP_TEST:5000/eth
curl -s $EC2_IP_TEST:5000/btc
curl -s $EC2_IP_TEST:5000/ada
curl -s $EC2_IP_TEST:5000/xrp
