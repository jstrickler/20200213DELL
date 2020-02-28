#!/usr/bin/env python
# import requests

mary_in = open('DATA/mary.txt')
# ...
mary_in.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)


# response = requests.get("http://blahblah")
# data = response.content

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("FORMATTED:")
    print(contents)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print("lines with n/l")
    print(all_lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print("lines withOUT n/l")
    print(all_lines_without_nl)

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        term, last_name, first_name, dob, dod, birth_place, birth_state, took_office,left_office, party = line.split(':')
        print("{:2s} {:25s} {:10s} {}".format(term, first_name, last_name, party))
