#!/usr/bin/env python
celsius_string = input("Enter Celsius temp: ")
celsius = float(celsius_string)
fahrenheit = ((9 * celsius) / 5) + 32

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

