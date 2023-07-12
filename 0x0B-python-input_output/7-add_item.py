#!/usr/bin/python3
"""in this module a script that
adds all arguments to a Python list, and then save them to a file"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    file = open("add_item.json")
except Exception:
    file = open("add_item.json", "w")
    file.write("[]")
finally:
    file.close()
lis = load_from_json_file("add_item.json")
for i in range(len(sys.argv)):
    if i == 0:
        continue
    lis.append(sys.argv[i])
save_to_json_file(lis, "add_item.json")
