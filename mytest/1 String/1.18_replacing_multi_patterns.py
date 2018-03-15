import re

def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

# re.sub takes three mandatory parameters like this:
# re.sub(pattern, repl, string, count=0, flags=0)
# But in above code, it only passes two, the first one
# is a callback returns a dict, and re.sub calls it with a 
# re.MatchObject instance

print multiple_replace('a b c d e f g h i j', {'a':'1','f':'2'})

# In above method, you need to re-define one_xlat everytime 
# you call multiple_replace method. In reality, if you have 
# one dictionary and you need to use it to replace a lot of 
# strings, you wouldn't want do to this. so you in that way 
# you can use below example, where it creates a xlat closure.

def make_xlat(*args, **kwds):
    adict = dict(*args, **kwds)
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    def xlat(text):
        return rx.sub(one_xlat, text)
    return xlat

translate = make_xlat({'a':'1','f':'2'})
print translate('a b c d e f g h i j')