import string
import sets

allchars = string.maketrans('abc', '123')

# print allchars

aString = '123456789a'

print aString.translate(allchars, '1')

keep = sets.Set(map(ord, 'abc'))

print len(keep)