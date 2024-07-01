#!/usr/bin/python3
"""
Module to fetch the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0

# Sample usage:
if __name__ == "__main__":
    subreddit = "python"
    print(number_of_subscribers(subreddit))
