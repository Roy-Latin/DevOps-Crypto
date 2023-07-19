#!/usr/bin/bash -xe

# Set the timeout value (in seconds)
timeout=10

# Make curl requests with a timeout
curl -s --max-time $timeout 192.168.56.1

# Check patterns using grep and handle the cases
if ! curl -s --max-time $timeout 192.168.56.1 | grep -q Crypto; then
  echo "Error: Pattern 'Crypto' not found"
  exit 1
fi

if ! curl -s --max-time $timeout 192.168.56.1/eth | grep -q lalalal; then
  echo "Error: Pattern 'lalalal' not found"
  exit 1
fi

if ! curl -s --max-time $timeout 192.168.56.1/btc | grep -q Price; then
  echo "Error: Pattern 'Price' not found"
  exit 1
fi

if ! curl -s --max-time $timeout 192.168.56.1/ada | grep -q Price; then
  echo "Error: Pattern 'Price' not found"
  exit 1
fi

if ! curl -s --max-time $timeout 192.168.56.1/xrp | grep -q Price; then
  echo "Error: Pattern 'Price' not found"
  exit 1
fi
