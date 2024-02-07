#!/usr/bin/python3
"""
doc
"""
import requests


def top_ten(subreddit):
    """
    doc
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers).json()
    top_ten = r.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for title in top_ten:
        print(title.get('data').get('title'))
