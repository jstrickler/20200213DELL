#!/usr/bin/env python

x = 100

def spam():
    x = "Batman"

    print("in spam(): x is", x)
    y = 42


spam()


print("x is", x)
# print("y is", y)
print(spam())
n = spam()
print(n)
