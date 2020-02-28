#!/usr/bin/env python
import knightlib

def main():
    info = knightlib.read_data('DATA/knights.txt')
    knightlib.pretty_pretty(info)
    print(knightlib.get_element(info, 'Bedevere', 2))
    knightlib.print_title(info)


main()
