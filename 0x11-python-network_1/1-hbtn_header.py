#!/usr/bin/python3
"""urllib package"""
from urllib import request
from sys import argv

url = argv[1]
with request.urlopen(url) as resp:
    print(resp.headers.get('X-Request-Id'))
