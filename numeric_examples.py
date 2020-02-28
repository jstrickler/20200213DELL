#!/usr/bin/env python

i1 = 100
i2 = 0b100
i3 = 0x100
i4 = 0o100
print(i1, i2, i3, i4, '\n')

f0 = 123.456
f1 = 123.
f2 = .456
f3 = 1.2323e13

print(f0, f1, f2, f3, '\n')

a = 29
b = 9

import math

print(a + b)
print(a - b, b - a)
print(a * b)
print(a / b, round(a / b, 2))
print(a // b, math.ceil(a / b))
print(a ** b)
print(a ** 2, b ** 2, b ** .5)
print(a % b)

a += 1   #  a = a + 1
a -= 10  #  a = a - 10
a *= 12
a //= 3
print(a)

#  a++   a--
#  --a   ++a

# for i in range(10):
#     print(i)





