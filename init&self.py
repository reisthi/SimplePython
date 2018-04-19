"""This simply explains how __init__ and self work."""


class Human():
    """Every human, should have a name and gender as soon as they are born"""

    def __init__(self, name, gender):
        """self mainly uses the object that is being passed to the class"""
        self.name = name
        self.gender = gender

    def print_info(self):
        print(f"The name is: {self.name}")
        print(f"The gender is: {self.gender}")

    def print_description(self, text):
        print(text)


thiago = Human("Thiago", "Male")
thiago.print_info()
thiago.print_description("Blood type is OAB")
