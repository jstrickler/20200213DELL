#!/usr/bin/env python

s1 = "spam\n"
print(len(s1))
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'

print("It's a trap!")
print('It\'s a trap!')  # not as good....
print('Guido was the "BDFL" of Python')
print("""Guido's the "BDFL" of Python""")

query = """
select *
from customers
where state = 'GA'
"""
