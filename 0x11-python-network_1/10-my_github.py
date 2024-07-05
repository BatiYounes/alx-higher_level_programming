#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
Uses Basic Authentication with a personal access token as password.
Uses requests and sys packages.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        if 'id' in data:
            print(data['id'])
        else:
            print("None")
    except ValueError:
        print("None")
