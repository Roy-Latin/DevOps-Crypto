#!/bin/bash

BUCKET_NAME="helm-crypto-k8s"
DIRECTORY="charts"

# List all .tgz files in the specified directory and delete them one by one
gsutil ls "gs://$BUCKET_NAME/$DIRECTORY/*.tgz" | while read -r tgz_object; do
    gsutil rm "$tgz_object"
done
