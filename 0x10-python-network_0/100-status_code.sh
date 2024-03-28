#!/bin/bash

# Bash script to send a request to a URL and display only the status code of the response

# Usage: ./100-status_code.sh <URL>

# Make sure URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
