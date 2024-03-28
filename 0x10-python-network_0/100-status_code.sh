#!/bin/bash

# Bash script to send a request to a URL and display only the status code of the response

# Send request and extract status code
curl -s -o /dev/null -w "%{http_code}" "$1"
