#!/usr/bin/env python

def get_message():
    return "Hello, DELL world"

m = get_message()

print(m)


def dumb():
    pass

x = dumb()
print(x)

def hello():
    m = get_message()
    print(m)

x = hello()   #  call the function and get the return value
x = hello     #  the function object (NOT called)

# x = foo[]  get element by index
# x = foo()  call

print(type(hello))
print(type(hello()))

def greet(greeting):
    print(greeting, "world")

greet("Hello")
greet("Hiya")
greet("'sup")
greet(123)


def find_string(target_string, *file_names):
    found = []
    for file_name in file_names:
        with open(file_name) as file_in:
            for raw_line in file_in:
                if target_string in raw_line:
                    found.append(raw_line.rstrip())
    return found

found_strings = find_string('bird', 'DATA/parrot.txt', 'DATA/alice.txt')
print(found_strings)

def count(target, start=0, stop=None):
    pass

