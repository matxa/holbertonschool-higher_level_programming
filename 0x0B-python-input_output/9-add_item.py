#!/usr/bin/python3
"""appending to a list in a file"""
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


file_name = "add_item.json"
try:
    ls = load_from_json_file(file_name)
except Exception:
    ls = []
for arg in range(1, len(argv)):
    ls.append(argv[arg])
save_to_json_file(ls, file_name)
