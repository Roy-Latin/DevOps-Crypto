#!/bin/bash

command_output=$(helm status crypto-app 2>&1)

expected_error="Error: release: not found"

if [ "$command_output" = "$expected_error" ]; then
    helm install crypto-app crypto-site-helm/my-flask-app
else
    helm upgrade --recreate-pods crypto-app crypto-site-helm/my-flask-app
fi