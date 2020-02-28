#!/usr/bin/env python

actor = "Chris Hemsworth"

print(type(actor), len(actor))

print(actor)
print(actor.upper())
print(actor.count('h'))
print(actor.startswith("Chris"))
print(actor.startswith("Liam"))
print(actor.count('wort'))
print(actor.lower().count('h'))

x = "taco"
print(x.isalpha())
x = "wombat2"
print(x.isalpha())


#  thing      value of object
#  thing()    CALL the object

#  obj.method()   # specific to obj
#  obj.property   # variable attached to obj
#  global_function(obj)  # generic

s = "     All my exes live in Texas      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xyxxyyxxxyyyAll my exes live in Texasyyyxxxyyxxyx"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()

data = "green;purple;red;black;green;red;red"
values = data.split(';')
print(values)
print("Unique:", set(values), '\n')

words = "this is a test"
print(words.split(), '\n')
