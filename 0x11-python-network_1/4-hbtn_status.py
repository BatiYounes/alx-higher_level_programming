#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using requests package.
Displays the body of the response in a specific format.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text).__name__)
    print("\t- content:", response.text)
