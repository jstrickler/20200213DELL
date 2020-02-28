#!/usr/bin/env python

target = 'Virginia'

with open('DATA/presidents.txt') as potus_in:
    for raw_line in potus_in:
        line = raw_line.rstrip()
        if target in line:
            print(line)
