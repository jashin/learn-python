#!/usr/bin/python

print "hello!!!"

for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print str(i) + " is a prime number"

print "while"

i = 2
j = 2

while i < 100:
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        print str(i) + " is a Prime Number"
    i += 1

