
#!/usr/bin/env python
a = "Abercrombie"
b = 123.4288392
c = "wombat"
d = 12

print(a, b, c, d)
print("Next line")
print("Next line")

print("First line", end="/")
print("Second line", end="HUH?")
print("Third line")
print("Fourth line")

print(a, b, c, d)
print(a, b, c, d, sep="/")
print(a, b, c, d, sep="")
print(a, b, c, d, sep=", ")
print(a, b, c, d, sep="\n")
print("GOOD JOB")

print(b)
print("Answer is {}".format(b))
print("Answer is {:.2f}".format(b))

#  "format string {} {} {}".format(arg, arg, arg, ...)
print(d)

for i in 8, 123, 12, 19, 5, -3, 389283:
    print("Answer is {:4d}".format(i))


# FUBAR

for word in "foo", 'bar', 'spam', 'wombat':
    print("{:8s}|{:>8s}|{:^8s} ".format(word, word, word))

bar = 12
football = 95

print(bar, football)

