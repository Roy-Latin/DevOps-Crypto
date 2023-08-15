#!/bin/bash

command_output=$(helm status crypto-helm 2>&1)

expected_error="Error: release: not found"

if [ "$command_output" = "$expected_error" ]; then
    helm install crypto-helm my-flask-app/
else
    helm upgrade crypto-helm my-flask-app/
fi