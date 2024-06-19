#!/usr/bin/python3

"""
Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords
    Args:
        subreddit (str): the name of the subreddit
        word_list (list): list of keywords to count
        after (str): parameter used for pagination, indicates the start
                     point for the next of results
        counts (dict): dictionary to store counts of keywords
    """
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}" \
              f"/hot.json?limit=100&after={after}"

    headers = {'User-Agent': 'ysg'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()

    if 'data' not in data or 'children' not in data['data']:
        return

    posts = data['data']['children']
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title.split():
                counts[word.lower()] = counts.get(word.lower(), 0) + 1

    after = data['data']['after']
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(word, count)
