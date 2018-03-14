import re

def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

# re.sub takes three mandatory parameters like this:
# re.sub(pattern, repl, string, count=0, flags=0)
# But in above code, it only passes two, the first one
# is a callback returns a dict, I guess that is count as two? 

print multiple_replace('a b c d e f g h i j', {'a':'1','f':'2'})
