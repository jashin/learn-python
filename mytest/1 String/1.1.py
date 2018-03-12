import sets

myString = "my string"

# string support for iterable directly
for c in myString:
  print c

# list function
thelist = list(myString)

for l in thelist:
  print l

square = []
for x in range(10):
  square.append(x ** 2)

print square

# built in list comprehensions
square = [x ** 2 for x in range(10)]

print square

# built in map function
def func(s):
  return s + '1'


results = map(func, myString)
print results

# sets.Set
magic_chars = sets.Set('abracadabra')
poppins_chars = sets.Set('supercalifragilisticexpialidocious')
print ''.join(magic_chars & poppins_chars)

# the result is acrd, it's doing binary and operation, for example, the first element
# in magic_chars it's "a" which is 97 and in binary it's    1100001
# in the second set, it's s which is 115 and in binary it's 1110011
# so the and operation result is 110001 which is a