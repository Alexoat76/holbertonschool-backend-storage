#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it
"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """ Decorator function that counts the number of calls to
        a function that is passed as an argument
    """

    @wraps(method)  # Preserves the original function name and docstring
    def wrapper(url):
        """ Wrapper for decorator functionality
        """
        r.incr(f"count:{url}")  # increment the count for the url by 1
        # get the cached html for the url by key name "cached:url"
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            # return the cached html if it exists and is a string type
            return cached_html.decode('utf-8')

        html = method(url)  # get the html from the url if it is not cached
        # set the html to the cache for 10 seconds
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_calls  # decorator function
def get_page(url: str) -> str:  # get the html content of the url
    """
    Track how many times a particular URL was accessed in the key
    "count:{url}" and Cache the result with an expiration time of 10 seconds
    """
    req = requests.get(url)
    return req.text
