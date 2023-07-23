#!/usr/bin/bash -xe

# Get the LoadBalancer IP address
CLUSTER_IP=$(kubectl get service docker-app-service -o=jsonpath='{.status.loadBalancer.ingress[0].ip}')
# Check if CLUSTER_IP is empty, if it is, exit the script
if [ -z "$CLUSTER_IP" ]; then
    echo "Error: LoadBalancer IP not found. Exiting..."
    exit 1
fi

# Set the timeout value (in seconds)
timeout=10

# Make curl requests with a timeout
curl -s --max-time $timeout $CLUSTER_IP

# Check patterns using grep and handle the cases
if ! curl -s --max-time $timeout $CLUSTER_IP | grep -q Crypto; then
  echo "Error: Pattern 'Crypto' not found"
  exit 1
fi

if ! curl -s --max-time $timeout $CLUSTER_IP/eth | grep -q Price; then
  echo "Error: Pattern 'lalalal' not found"
  exit 1
fi

if ! curl -s --max-time $timeout $CLUSTER_IP/btc | grep -q Price; then
  echo "Error: Pattern 'Price' not found"
  exit 1
fi

if ! curl -s --max-time $timeout $CLUSTER_IP/ada | grep -q Price; then
  echo "Error: Pattern 'Price' not found"
  exit 1
fi

if ! curl -s --max-time $timeout $CLUSTER_IP/xrp | grep -q Price; then
  echo "Error: Pattern 'Price' not found"
  exit 1
fi
