"""
Args and kwargs simply allow functions to accept optional arguments,
so you can create flexible APIs in your modules and classes.
"""


def bar(required, *args, **kwargs):
    print("required:", required)
    if args:
        print("args:", args)
    if kwargs:
        print("kwargs:", kwargs)


# example 1:
bar()  # This will give an error

# example 2:
bar('hello')  # hello

# example 3:
bar('hello', 1, 2, 3)  # hello (1, 2,3)

# example 4:
bar('hello', 1, 2, 3, key='key', another_key=999)  # hello (1, 2, 3) {'key': 'key', 'another_key': 999}


def another_test(required, *args, **kwargs):
    """ Simple test for all objects """

    print("required: ", required)
    if args:
        print("args: ", args)
        if kwargs:
            print("kwargs: ", kwargs)


a_string = 'this is my string!'
a_integer = 454333
a_tuple = {(0, 1), (2, 3)}
a_list = (0, 1, 2, 3, 4,)
another_tuple = {'key': 'value', 'key1': 'value', 'key2': 'value'}


another_test(a_string, a_integer, a_tuple, a_list, another_tuple)
