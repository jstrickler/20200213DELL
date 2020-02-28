#!/usr/bin/env python
from pprint import pprint

def read_data(file_name):
    knight_data = {}

    with open(file_name) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment

    return knight_data

def pretty_pretty(data):
    pprint(data)
    print()

def get_element(data, knight, field):
    return data[knight][field]

def print_title(data):
    for name, data in data.items():
        print(data[0], name)
