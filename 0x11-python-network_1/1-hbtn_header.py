#!/usr/bin/python3
"""urllib package"""

import urllib
import sys
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as resp:
        print(resp.headers.get('X-Request-Id'))
