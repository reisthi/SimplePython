"""
    Some underscore usage in python
"""


#  Single leading underscore: _var
#  Single leading underscores are just a way for the programmer to know that variable is meant to be used internally

#  Single trailing underscore: var_
#  Single trailing underscore are used by convention to avoid naming conflicts


#  Double leading underscore: __var
#  Double leading underscores protects the variable so it is not overridden by subclasses
class Test:
    """Example of a leading underscore usage"""
    def __init__(self):
        self.foo = 1
        self._foos = 2
        self.__fooz = 3  # this var won't be accessible unless you call __Test__fooz

