"""
Both str and repr are meant to be string representations of a class.
The difference between those is that str is a more of a str representation to the user,
while repr is more of a str representation for the developer in order to avoid possible ambiguity of an object.
"""


class ClassOne:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def __repr__(self):
        return f'({self.foo!r}), {self.bar!r}'
        # the !r is to force the output to be a repr instead of a str representation

    def __str__(self):
        return f'{self.foo}, {self.bar}'


# here is a even better repr for a class
class ClassTwo:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def __repr__(self):
        return (f'{self.__class__.__name__}(',
                f'{self.foo!r}, {self.bar!r}')
    # this will also return the name of the class without worring if it ever changes
