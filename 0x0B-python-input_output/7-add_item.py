#!/usr/bin/python3
"""adds all arguments to a Python list,
and then save them to a file
"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    filename = "add_item.json"
    newlist = sys.argv[1:]
    try:
        oldata = list(load(filename))
    except FileNotFoundError:
        f = open(filename, 'x', encoding="UTF8")
        f.close()
        oldata = []
    oldata += newlist
    save(oldata, filename)
