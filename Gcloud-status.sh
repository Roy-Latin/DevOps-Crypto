#!/bin/bash -xe

# Check if all Flask pods are in the Running state
while [[ "$(kubectl get pods -l app=flask-app -o 'jsonpath={..status.phase}')" != "Running Running" ]]; do
  echo "Flask pods are still not Running"
  sleep 10
done

echo "Flask pods are Running"

# Check if the MySQL pod is in the Running state
while [[ "$(kubectl get pods -l app=mysql -o 'jsonpath={..status.phase}')" != "Running" ]]; do
  echo "MySQL pod are still not Running"
done

echo "MySQL pod are Running"

echo "Pods are all Running"
