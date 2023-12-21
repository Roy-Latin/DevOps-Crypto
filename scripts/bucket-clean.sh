#!/bin/bash

BUCKET_NAME="roys-crypto-site"

# List all .tgz files in the specified directory and delete them one by one
gsutil ls "gs://$BUCKET_NAME/*.tgz" | while read -r tgz_object; do
    gsutil rm "$tgz_object"
done
