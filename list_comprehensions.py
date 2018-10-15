"""Comprehending comprehensions"""

squares = [x * x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = [x * x for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# sets with list comprehensions
a_set = {x * x for x in range(-9, 10)}
# {64, 1, 0, 36, 4, 9, 16, 81, 49, 25}

# dictionaries
a_dict = {x: x * x for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

