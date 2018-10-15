"""Arrays have the same functionality as lists with one exception,
    they are typed arrays, which means they only accept one type of data"""

import array

# build an array
arr = array.array('f', (0, 1, 2, 3))
print(arr[1])  # 1.0

# arrays are mutable
arr[1] = 24
print(arr)  # array('f', [0.0, 24.0, 2.0, 3.0])

del(arr[1])
print(arr)  # array('f', [0.0, 2.0, 3.0])

# arrays are typed, only take one type of data
arr[1] = "let's try a string"
# TypeError: must be real number, not str


