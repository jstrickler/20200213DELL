#!/usr/bin/env python
import sys

list1 = list()
print(list1, len(list1))
list2 = ['wombat', 'weasel', 'walrus', 'wolf', 'wolverine']
print(list2, len(list2))
list3 = []
mongoose = "a b c d"
list4 = mongoose.split()
print(list4)

cities = ['Austin', 'Bastrop', 'San Antonio']
cities.append("New Braunfels")
cities.append("Hutto")
print(cities)
cities.insert(0, "Pflugerville")
cities.insert(4, "Luckenback")
cities.insert(4, "Levelland")
more_cities = ['Georgetown', 'Fredericksburg', 'Kerrville']
print(cities)
cities.extend(more_cities)
print(cities)
print(cities[5])
del cities[5]   # del THING
cities.remove("Hutto")
print(cities)
c = cities.pop()
print(c)
print(cities)
c = cities.pop(2)
print(c)
print(cities)
cities[0] = "Jerrel"
print(cities)

print(sys.maxsize)

flags = [True] * 25
print(flags)

print(['a', 'b', 'c'] * 4)

print(cities)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[9])
print(fruits[-1], fruits[-2], fruits[len(fruits)-1])

#  SEQUENCE[START:STOP]    S[START:]   S[:STOP]
#  S[START:STOP:STEP]
print(fruits)
print(fruits[0:3])  # first 3
print(fruits[6:10]) # 4 starting at 6
print(fruits[:3])
print(fruits[12:])

word = "(spam)"
print(word[1:-1])
print(sys.argv)

args = sys.argv[1:]
print(args)
for file_name in args:
    print(file_name)
print()

print(sys.argv)
search_term = sys.argv.pop(1)
print("search term:", search_term)
for file_name in sys.argv[1:]:
    print(file_name)
print()

for city in cities:
    # city = next(cities)
    print(city)
print()

print(fruits)
print(fruits[::])
print(fruits[::2])
print(fruits[1::2])

x = fruits
y = fruits[::]
y.append("durian")
print(fruits)
print(y)

#   SEQ[START:STOP:STEP]
#   SEQ(0:len(SEQ):1]

print(fruits[10:5:-1])
print(fruits[5:10:-1])
print(fruits[15:99])

result = fruits[:5] + fruits[-5:]
print(result)


word = "shampoo"

for letter in word:
    print(letter)

x = []
x.append(['a', 'b', 'c'])
x.append(['d', 'e', 'f'])
x.append(['g', 'h', 'i'])
print(x)
print(len(x))
print(x[0])
print(x[0][0])
print(x[-1][-1])
print(x[-1])
x[1].append('wombat')
x[-1].insert(2, 'spam')
print(x)

y = "12"
for thing in x:
    # thing = <next value of iterable x[1]
    print(thing)

actor = "Brad Pitt"
print(actor[:4])
print(actor[-4:])
