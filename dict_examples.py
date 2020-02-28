#!/usr/bin/env python

d1 = dict()
print(d1)
d2 = {'TX': 'Austin', 'NC': 'Raleigh', 'MT': "Helena"}
d3 = {}

d2['CA'] = 'Sacramento'
d2['OR'] = 'Salem'
d2['WA'] = 'Olympia'

airports = {
    'EWR': 'Newark',
    'YYC': 'Calgary',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YOW': 'Ottawa',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
}

airports['AUS'] = "Austin"
print(airports)

print(airports['MCI'])

airports['LOS'] = 'Los Angeles'
airports['LAX'] = airports['LOS']
del airports['LOS']

my_vars = {}
my_vars['x'] = 5

# print(airports['CLE'])
print(airports.get('CLE'))
print(airports.get('CLE', 42))

print(airports.setdefault('CLE', 'Cleveland'))
print(airports)

more_airports = {'PHX': 'Phoenix', 'SFO': 'San Francisco',
                 'TPA': 'Tampa'}

airports.update(more_airports)

print(airports)


for abbr in 'PXH', 'RDU', 'AUS', 'QAD', 'BZN':
    print(abbr, abbr in airports)
print()

del airports['MCO']
print(airports)

print(len(airports), '\n')

for k, v in airports.items():
    print(k, v)
print()

print(airports.items())

for k, v in sorted(airports.items()):
    print(k, v)
print()

def by_value(wombat):
    return wombat[1], wombat[0]

for k, v in sorted(airports.items(), key=by_value):
    print(k, v)
print()




