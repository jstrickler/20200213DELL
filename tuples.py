#!/usr/bin/env python

# tuple-o honey!

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'
print(person)
print(type(person))
print(person[0], person[-1])


first_name, last_name, product, dob = person   # iterable unpacking

x = ['a', 'b']

i, j = x
i = x[0]
j = x[1]



people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('mark', 'zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
print(people[0])
print(people[0][0])
print(people[0])
print(people[0][0][0])
print(people[0][0][0][0])
print(people[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0])
print(people[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1])
print()

# for person in people:
#     print(person[0], person[1])
# print('-' * 60)
#
# for person in people:
#     first_name, last_name, product, dob = person
#     print(first_name, last_name)
# print('-' * 60)

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print('-' * 60)

x = [('a', 5), ('b', 2), ('c', 8)]
for weasel, ocelot in x:   # weasel = x[0][0], ocelot = x[0][1]
    print(weasel * ocelot)
print('-' * 60)

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

word = "toast"
print(len(values), len(people), len(person), len(word))

print(min(people), max(people))
nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(min(nums), max(nums))

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

print(min(fruits), max(fruits))
print(sum(nums))

print(sorted(fruits))
print(sorted(nums))

def ignore_case(person):
    return person[1].lower(), person[0].lower()

for first_name, last_name, *_ in sorted(people, key=ignore_case):
    print(first_name, last_name)
print('-' * 60)

x = ['a', 'b', 'c']
for char in reversed(x):
    print(char)
print()
print(reversed(x))

r = reversed(x)
print(r)
for m in r:
    # m = next(r)    r.__next__()....
    print(m)

print(x, '\n')

for thing in x:
    print(thing)   #print() auto-adds newline
print()

for i, thing in enumerate(x):
    print(i, thing)
print()

print(list(enumerate(x)))
print(list(reversed(x)))

r = reversed(x)
print("first try:")
for c in r:
    print(c)

print("second try:")
for c in r:
    print(c)

r = reversed(x)
v = list(reversed(x))
print(type(r), type(v))
print()

x = ['a', 'b', 'c']

r1 = reversed(x)
r2 = reversed(x)
r3 = reversed(x)
e = enumerate(x)

x.append('d')
x.append('e')

for letter in r1:
    print(letter)


for i, letter in e:
    print(i, letter)
print(list(enumerate(x))
      )
