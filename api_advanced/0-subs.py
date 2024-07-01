#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers or 0 if the subreddit is not found or any error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError, KeyError):
        return 0

