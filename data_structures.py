"""Book recommendation: The Algorithm Design Manual by Steven S. Skiena"""

# dictionaries
squares = {x: x * x for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

"""
Ordered Dictionaries: OrderedDict
    * preserves the order of insertion 
    * allows insertion of new items
"""

import collections

d = collections.OrderedDict(one=1, two=3, three=3)
# OrderedDict([('one', 1), ('two', 3), ('three', 3)])
d.keys()
# odict_keys(['one', 'two', 'three'])
d['four'] = 4
# OrderedDict([('one', 1), ('two', 3), ('three', 3), ('four', 4)])

"""
Default Dictionaries: defaultdict
    * accepts a callable in its constructor
"""
from collections import defaultdict

dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin ')
dd['dogs'].append('Mr Sniffles')

print(dd['dogs'])
# ['Rufus', 'Kathrin ', 'Mr Sniffles']
