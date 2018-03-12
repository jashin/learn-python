import sys
import os
sys.path.append('lib')

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/lib/animals/pets/')

import dog

print sys.path

dog.bark()

# pets.cat.purr()