import string

msg = string.Template('the square of $number is $square')

for number in range(10):
    square = number * number
    print msg.substitute(locals())

print '------------------'

for i in range(10):
    print msg.substitute(number=i, square=i*i)

print '------------------'

for number in range(10):
    print msg.substitute(locals(), square=number*number)

print '------------------'

msgA = string.Template('an $adj $msgA')
adj = 'interesting'
print msgA.substitute(locals(), msgA='message')
