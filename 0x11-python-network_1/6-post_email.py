#!/usr/bin/python3
"""
Script that sends a POST request to a URL with an email as a parameter.
Uses requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}  # Ensure correct headers

    try:
        response = requests.post(url, data=payload, headers=headers)

        print(f"Your email is: {email}")
        print(response.text.strip())  # Remove extra whitespace from response

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
