#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit
"""

import requests
from sys import argv
import json


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    Args:
        subreddit (str): the name of the subreddit
    Returns:
        int: the number of subscribers, or 0 if the subreddit is invalid
    """
    subreddit = "programming"
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': '0-subs/1.0 (by /u/yaasgyan)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    print("Response status code:", response.status_code)
    # data = response.json()
    if response.status_code >= 300:
        return (0)
    data = response.json()
    data_dict = data.get('data', {}).get('subscribers', 0)
    return(data_dict)


if __name__ == "__main_":
    subscribers = number_of_subscribers()
    print(subscribers)
