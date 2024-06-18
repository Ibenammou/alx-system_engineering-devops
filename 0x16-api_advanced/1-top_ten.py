#!/usr/bin/python3
"""
Queries the Reddit API and print the titles of the first 10
hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit
    Args:
        subreddit (str): the name of the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'queenbae'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    if 'data' not in data or 'children' not in data['data']:
        print(None)
        return

    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])
