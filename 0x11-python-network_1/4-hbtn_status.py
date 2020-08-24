#!/usr/bin/python3
"""request package"""
import requests


if __name__ == "__main__":
    res = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('	- type: {}'.format(type(res.text)))
    print('	- content: {}'.format(res.text))
