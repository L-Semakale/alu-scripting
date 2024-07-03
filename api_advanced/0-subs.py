#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers, or 0 if the subreddit does not exist.
    """
    user_agent = "Mozilla/5.0 (x11; Linux x86_64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    url = f"https://api.reddit.com/r/{subreddit}/about"

    headers = {"User-Agent": user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    data = response.json()
    return data['data']['subscribers']

# Example usage
print(f"Subscribers in 'python': {number_of_subscribers('python')}")
print(f"Subscribers in 'nonexistentsubreddit': {number_of_subscribers('nonexistentsubreddit')}")
