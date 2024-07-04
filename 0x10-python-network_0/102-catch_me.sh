#!/bin/bash
# Script to make a request to 0.0.0.0:5000/catch_me and display the response

curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
