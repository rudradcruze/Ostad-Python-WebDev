# Errors vs Exceptions

try:
    with open("name.txt") as file:
        print(file.read())
    print(10/10)
    x = int("10")
    a = [1, 2, 3]
    print(a[1])
    # b = abc
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("You can't divide by zero")
except FileNotFoundError:
    print("The file does not exist")
except IndexError:
    print("The index is out of range")
except NameError:
    print("The variable is not defined")
except Exception as e:
    print("Some error occurred! ", e)