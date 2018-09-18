"""
Shallow copy is a one level deep copy. I won't copy child objects.
Deep copy will copy the child objects, but is a slower process.
"""

import copy

# Shallow Copy #
# example of a shallow copy 1
a = [[1, 2, 3], ['a', 'b', 'c']]
b = list(a)
print(b)  # this will return [[1, 2, 3], ['a', 'b', 'c']]

# example of a shallow copy 2
a.append(['this is new'])
print(a)  # [[1, 2, 3], ['a', 'b', 'c'], ['this is new']]
print(b)  # [[1, 2, 3], ['a', 'b', 'c']]
# as you can see z was not copied to b

# example of a shallow copy 3
a[0][1] = 'X'  # [[1, 'X', 3], ['a', 'b', 'c']] ['this is new']]
# now look what happens when we print b
print(b)  # [[1, 'X', 3], ['a', 'b', 'c']]

# Deep Copy #
# import copy
c = copy.deepcopy(a)  # creates an independent copy where changes won't affect the cloned version(c)
a.append(['This is new'])
print(a)  # [[1, 'X'], ['a', 'b', 'c'], ['this is new']]
print(b)  # [[1, 'X'], ['a', 'b', 'c']]

# and it won't reflect changes either
a[0][1] = 'X'
print(a)  # [[1, 'X', 3], ['a', 'b', 'c'], ['this is new']]
print(b)  # [[1, 2, 3], ['a', 'b', 'c'], ['this is new']]
