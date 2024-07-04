#!/bin/bash
# Script to send a JSON POST request to a URL and display the body of the response

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

URL="$1"
JSON_FILE="$2"

curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"
