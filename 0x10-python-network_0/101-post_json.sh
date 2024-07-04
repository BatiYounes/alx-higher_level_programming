#!/bin/bash
# Script to send a JSON POST request to a URL and display the body of the response
[ "$#" -eq 2 ] && curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
