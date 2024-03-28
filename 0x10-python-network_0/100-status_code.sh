#!/bin/bash

# Bash script to send a request to a URL and display only the status code of the response

# Usage: ./100-status_code.sh <URL>

# Make sure URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request and store response in a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" -w "%{http_code}" "$1"

# Extract and display status code
status_code=$(cat "$response_file")
echo "$status_code"

# Clean up temporary file
rm "$response_file"
