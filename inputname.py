""" This simply gets an input name and mess with it"""

print("***************************")
print("Welcome to the first project")
print("***************************")

name = input("What is your name? ")

age = int(input("What is your age? "))

user_age = str(age)

year = str((2017 - age) + 100)

print(name + ", you will be  100 years old in " + year)
print(4 * " string")