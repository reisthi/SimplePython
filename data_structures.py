"""Book recommendation: The Algorithm Design Manual by Steven S. Skiena"""

# dictionaries
squares = {x: x * x for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# *****************************************************************

#
# Ordered Dictionaries: OrderedDict
#     * preserves the order of insertion
#     * allows insertion of new items

import collections

d = collections.OrderedDict(one=1, two=3, three=3)
# OrderedDict([('one', 1), ('two', 3), ('three', 3)])
d.keys()
# odict_keys(['one', 'two', 'three'])
d['four'] = 4
# OrderedDict([('one', 1), ('two', 3), ('three', 3), ('four', 4)])

# *****************************************************************

# Default Dictionaries (defaultdict)
#     * accepts a callable in its constructor

from collections import defaultdict

dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin ')
dd['dogs'].append('Mr Sniffles')

print(dd['dogs'])
# ['Rufus', 'Kathrin ', 'Mr Sniffles']

# *****************************************************************

# ChainMap
#     * allows search multiple dictionaries as a single mapping
from collections import ChainMap

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
dict3 = {'eleven': 11, 'five': 5}

chain = ChainMap(dict1, dict2)
print(chain)
# ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

print(chain['three'])  # Searches each collection from left to right until it finds the key or fails
# 3

print(chain['missing'])
# KeyError: 'missing'

# *****************************************************************

# MappingProxyType
#     * Mapper for read-only dictionaries
from types import MappingProxyType
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

print(read_only['one'])
# 1
# read_only['one'] = 22
# TypeError: 'mappingproxy' object does not support item assignment

