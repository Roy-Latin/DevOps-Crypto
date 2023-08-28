#!/bin/bash

# Get the new version number from Jenkins or any other source

# Update the version in charts.yaml
sed -i "s/version: [0-9]\+\.[0-9]\+\.[0-9]\+/version: 0.1.${BUILD_NUMBER}/g" my-flask-app/Chart.yaml
