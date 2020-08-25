#!/usr/bin/python3
"""request package"""
import requests
import sys
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    respond = requests.get(url, auth=(argv[1], argv[2]))
    res_json = respond.json()
    if res_json:
        print("{}".format(res_json.get('id')))
