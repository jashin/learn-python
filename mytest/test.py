from test_class import TestClass
# import copy

t = TestClass
t.tpl = (1, 2, 3, 4, 5)
t.lst = [1, 2, 3, 4]

t.lst.append(5)

# print t.lst

list_of_lists = [['a'], [1, 2], ['z', 23]]

copy_lol = list(list_of_lists)
copy_lol.append('abc')
copy_lol[1].append(2)
print copy_lol
print list_of_lists

a1, a2, a3, a4 = [1, 2, 3, 4]

print a3