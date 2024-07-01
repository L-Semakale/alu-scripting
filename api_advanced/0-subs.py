mport requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers.
    """
    user_agent = "Mozilla/5.0 (x11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    URL = f"https://api.reddit.com/r/{subreddit}/about"
    
    headers = {"User-Agent": user_agent}
    
    response = requests.get(URL, headers=headers, allow_redirects=False)
    data = response.json()
    return data['data']['subscribers']

# Example usage
print(number_of_subscribers('python'))
