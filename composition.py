""" Simple example of using composition.

    When to use composition instead of inheritance?
    - Whenever you have very distinguished models
    - Package code into modules that are unrelated

"""


class Parent(object):

    def first(self):
        print("This is the first function.")

    def override(self):
        print("This comes from PARENT.")

    def altered(self):
        print("This altered() comes from PARENT")


class Child(object):

    def __init__(self):
        self.parent = Parent()

    def first(self):
        self.parent.first()

    def override(self):
        print("This comes from CHILD.")

    def altered(self):
        print("CHILD BEFORE calling altered()")
        self.parent.altered()
        print("CHILD AFTER altered()")


# >>> from composition import *
# >>> son = Child()
# >>> son.first()
# This is the first function.
# >>> son.override()
# This comes from CHILD.
# >>> son.altered()
# CHILD BEFORE calling altered()
# This altered() comes from PARENT
# CHILD AFTER altered()
