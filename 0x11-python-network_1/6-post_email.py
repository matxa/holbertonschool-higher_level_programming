#!/usr/bin/python3
"""request package"""
import requests
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=data)
    print(res.text)
