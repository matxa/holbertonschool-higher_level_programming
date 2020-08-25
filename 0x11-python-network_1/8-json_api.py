#!/usr/bin/python3
"""request package"""
import requests
import sys
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    data = {'q': q}
    try:
        respond = requests.post("http://0.0.0.0:5000/search_user", data)
        res_json = respond.json()
        if res_json:
            print("[{}] {}".format(res_json.get('id'), res_json.get('name')))
        else:
            print("Not a valid JSON")
    except:
        print("No result")
