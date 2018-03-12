import sys
from chainmap import Chainmap 

mapTest = Chainmap([11, 22, 33], [2, 3, 4], (5, 6, 7))

# print mapTest.get(2)

mapTest2 = Chainmap({"a": 1, "b": 2}, {"c": 3}, {"d": 4})

print mapTest2.get("d")
print mapTest2["d"]

print "d" in mapTest2

# it doens't have __iter__ in chainmap
# for k in mapTest2:
#   print k
# mapTest2["d"] = 5
