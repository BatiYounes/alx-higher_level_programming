#!/bin/bash

# Bash script to send a request to a URL and display only the status code of the response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request and extract status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")
echo "$status_code"
