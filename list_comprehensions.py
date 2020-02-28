#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

#  [EXPRESSION for VAR in ITERABLE if CONDITION]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

fgen = (f.upper() for f in fruits if f.startswith('p'))
print(fgen)
for fruit in fgen:
    print(fruit)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print(last_names, '\n')

names_gen = ('{} {}'.format(p[0], p[1]) for p in people)

for name in names_gen:
    print(name)


nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

#  [EXPR for VAR in ITERABLE if COND]
large_nums = sorted([float(n * 10) for n in nums if n > 300])
print(large_nums, '\n')
