s = '   123    '

print s.lstrip()
print s.rstrip()
print s.strip()

s = 'ab dasdf asdf asdf asdf asdf asdf d'

print s.strip('a')
print s.strip('ab')
print s.strip('abd')
print s.strip('abd ')