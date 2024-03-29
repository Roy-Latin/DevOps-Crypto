#!/bin/bash

# Get the new version number from Jenkins or any other source

# Increment the patch version based on the build number
VERSION="0.1.$BUILD_NUMBER"

# Update the version in charts.yaml
sed -i "s/version: [0-9]\+\.[0-9]\+\.[0-9]\+/version: $VERSION/g" my-flask-app/Chart.yaml
