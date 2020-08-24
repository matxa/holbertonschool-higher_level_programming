#!/usr/bin/python3
"""urllib package"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as resp:
        print(resp.headers.get('X-Request-Id'))
