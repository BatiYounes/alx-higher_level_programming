#!/usr/bin/python3
"""
Fetch and print the 10 most recent commits from a specified GitHub repository.
"""
import requests
import sys


def fetch_commits(repo, owner):

    """
    Fetch the 10 most recent commits from a specified GitHub repository.

    Args:
        repo (str): The repository name.
        owner (str): The owner of the repository.

    Returns:
        list: A list of dictionaries containing commit SHAs and author names.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    commits = response.json()
    return commits[:10]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo> <owner>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]

    commits = fetch_commits(repo, owner)
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit', {}).get('author', {}).get('name')
        print(f"{sha}: {author_name}")
