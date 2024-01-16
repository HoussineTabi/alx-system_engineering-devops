#!/usr/ben/python3
"""
Task number 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyAPIUserAgent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except:
        return 0


if __name__ == "__main__":
    print()
