#!/usr/bin/python3
"""
This module provides a function to get the number of subscribers for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit does not exist, it returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'my-app-0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"Data: {data}")  # Debugging line
        return data['data'].get('subscribers', 0)
    else:
        return 0
