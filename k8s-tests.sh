#!/usr/bin/bash -xe

# Function to get the LoadBalancer IP
get_loadbalancer_ip() {
    kubectl get service flask-app-service -o=jsonpath='{.status.loadBalancer.ingress[0].ip}'
}

# Check if the LoadBalancer IP is empty and wait until it becomes available
while [ -z "$(get_loadbalancer_ip)" ]; do
    echo "Waiting for LoadBalancer IP to be assigned..."
    sleep 10
done

# Get the LoadBalancer IP address
CLUSTER_IP=$(get_loadbalancer_ip)

# Check if CLUSTER_IP is still empty (could be a timeout case) and exit the script
if [ -z "$CLUSTER_IP" ]; then
    echo "Error: LoadBalancer IP not found. Exiting..."
    exit 1
fi

echo "LoadBalancer IP: $CLUSTER_IP"
# Continue with your script logic after obtaining the LoadBalancer IP

sleep 15

# Set the timeout value (in seconds)
timeout=15

# Make curl requests with a timeout
curl -s --max-time $timeout $CLUSTER_IP

# Check patterns using grep and handle the cases
if ! curl -s --max-time $timeout $CLUSTER_IP | grep -q Crypto; then
  echo "Error: Pattern 'Crypto' not found"
  exit 1
fi

if ! curl -s --max-time $timeout $CLUSTER_IP/eth | grep -q Price; then
  echo "Error: Pattern 'Price' not found"
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
