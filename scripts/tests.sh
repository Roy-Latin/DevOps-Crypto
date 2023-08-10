#!/usr/bin/bash -xe
curl -s $EC2_IP_TEST:5000
curl -s $EC2_IP_TEST:5000 | grep Crypto
curl -s $EC2_IP_TEST:5000/eth | grep $
curl -s $EC2_IP_TEST:5000/btc | grep $
curl -s $EC2_IP_TEST:5000/ada | grep $
curl -s $EC2_IP_TEST:5000/xrp | grep $
