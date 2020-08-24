#!/usr/bin/python3
"""urllib package"""
import urllib
import sys
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with request.urlopen(url, data) as respose:
        print(respose.read().decode('utf-8'))
