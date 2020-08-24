#!/usr/bin/python3
"""urllib package"""
import urllib
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as resp:
        resp_read = resp.read()
        print("Body response:")
        print("	- type: {}".format(type(resp_read)))
        print("	- content: {}".format(resp_read))
        print("	- utf8 content: {}".format(resp_read.decode('utf-8')))
