#!/usr/bin/python3
"""request package"""
import requests


if __name__ == "__main__":
    with requests.get('https://intranet.hbtn.io/status') as res:
        print('Body response:')
        print('	- type: {}'.format(type(res.text)))
        print('	- type: {}'.format(res.text))
