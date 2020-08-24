#!/usr/bin/python3
"""urllib package"""
import urllib
from urllib import request


url = 'https://intranet.hbtn.io/status'
with request.urlopen(url) as resp:
    resp_read = resp.read()
    body_resp = {
        'type': type(resp_read),
        'content': resp_read,
        'utf8': resp_read.decode('utf-8')
    }
    print("Body response:")
    for k, v in body_resp.items():
        print("\t- {}: {}".format(k, v))
