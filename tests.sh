#!/usr/bin/bash -xe
curl -s ${env.EC2_IP_TEST}:5000
curl -s ${env.EC2_IP_TEST}:5000 | grep Crypto
curl -s ${env.EC2_IP_TEST}:5000/eth
curl -s ${env.EC2_IP_TEST}:5000/btc
curl -s ${env.EC2_IP_TEST}:5000/ada
curl -s ${env.EC2_IP_TEST}:5000/xrp
