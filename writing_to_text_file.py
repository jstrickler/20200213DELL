#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


with open('fruits.txt', "w") as fruits_out:
    fruits_out.write("durian\n")
    fruits_out.write("elderberry\n")
    for fruit in fruits:
        fruits_out.write(fruit + '\n')


