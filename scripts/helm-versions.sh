#!/bin/bash

# Get the new version number from Jenkins or any other source
NEW_VERSION=0.1.${BUILD_NUMBER}  # Replace this with the actual new version

# Update the version in charts.yaml
sed -i "s/version: [0-9]\+\.[0-9]\+\.[0-9]\+/version: $NEW_VERSION/g" DevOps-Crypto/my-flask-app/Chart.yaml
