""" This tests if a number is even or odd"""

print("***************")
print("EVEN or ODD?")
print("***************")


def evenoddtest():
    number = int(input("Type a number: "))
    remainder = number % 2
    result = str(number)

    if remainder == 1:
        print(result + " is odd.")
    else:
        print(result + " is even.")

    rerun = input("Type 1 to check again.")
    if rerun == 1:
        evenoddtest()
