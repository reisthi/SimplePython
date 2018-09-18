"""
Lambda functions behave just like regular functions. They are small, anonymous functions.
They are single expression functions
"""

add = lambda x, y: x + y
add(5, 3)  # This will return 8

(lambda x, y: x + y)(5, 3)  # This will also return 8

tuples = [(1, 'z'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted(tuples)  # this will sort by x[0]
# [(1, 'z'), (2, 'b'), (3, 'c'), (4, 'a')]


sorted(tuples, key=lambda x: x[1])  # this will sort by x[1]
# [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'z')]


