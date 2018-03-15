import re

#Comparing the non-class based code, this code has better reusability, 
# e.g. in previous code, if you have multiple dictionaries, and you 
# create multipe make_xlat instances, one for each dict, now you want 
# to change how the regex is composed, you have to make a copy of 
# make_xlat definiation and update it. But with class version, 
# you can just use a sub class.

class make_xlat:
    def __init__(self, *args, **kwd):
        self.adict = dict(*args, **kwd)
        self.rx = self.make_rx()
    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.adict)))
    def one_xlat(self, match):
        return self.adict[match.group(0)]
    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)

class make_xlat_by_whole_words(make_xlat):
    def make_rx(self):
        return re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, self.adict)))

translate = make_xlat({'a':'1','f':'2'})
print translate('aa b c d e f g h i j')

translate_wholeword = make_xlat_by_whole_words({'a':'1','f':'2'})
print translate_wholeword('aa b c d e f g h i j')