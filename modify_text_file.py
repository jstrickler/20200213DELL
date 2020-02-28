#!/usr/bin/env python

with open('fruits.txt') as fruits_in:
    with open('newfruits.txt', 'w') as fruits_out:
        for line in fruits_in:
            replacement_line = line.replace('e', 'X')
            fruits_out.write(replacement_line)
