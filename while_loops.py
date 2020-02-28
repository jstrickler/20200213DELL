#!/usr/bin/env python

#  if COND:
#     code...

# while COND:
#     code ...

while True:
    name = input("What is your name? (or q to quit) ")
    if name == 'q':
        break   # exit loop
    if name == '':
        continue  # go back to top
    print("Welcome,", name)

