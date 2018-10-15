"""Slicing tricks"""

# [start:stop:step]

# [::2] goes from beginning to the end jumping 2 indexes
a_list = [1, 2, 3, 4, 5]

# [::] goes from beginning to the end
print(a_list[::])  # [1, 2, 3, 4, 5]

# [::2] goes from beginning to the end jumping 2 indexes
print(a_list[::2])  # [1, 3, 5]

# list in reverse order
print(a_list[::-1])  # [5, 4, 3, 2, 1]

# del a_list[:] deletes elements in a list but not the list itself
del a_list[:]
print(a_list)  # []

# del a_list[::2] deletes elements by jumping two indexes
# [2, 4]


