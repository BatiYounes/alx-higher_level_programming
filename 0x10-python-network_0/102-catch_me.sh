#!/bin/bash

# Bash script to make a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing "You got me!".

# Send request with custom header
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "http://0.0.0.0:5000/catch_me"
