#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    title of all hot articles for a given subreddit
    Args:
        subreddit (str): the name of the subreddit
        hot_list (list): list to store the titles of the hot articles
        after (str): parameter used for pagination, indicates the start
                    point for the next page of results
    Returns:
        list: list containing the titles of all hot articles for the subreddit
                or None if no results are found
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'Ysg'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()

    if 'data' not in data or 'children' not in data['data']:
        return None

    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after is None:
        return hot_list
    else:
        return (recurse(subreddit, hot_list, after))
