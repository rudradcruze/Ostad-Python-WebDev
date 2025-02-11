x = 10

print(x)

def myfunc():
    x = 5
    y = 110
    print(y)
    print(x)
    x = 15

myfunc()
print(x)

# LEGB Rule
# L: Local
# E: Enclosing
# G: Global
# B: Built-in


n = "Global Variable"

def myfunc():
    n = "Enclosing Variable"
    def myinnerfunc():
        # global n # This will change the value of n in the global scope.
        nonlocal n # This will change the value of n in the enclosing scope.
        n = "Local Variable"
        print(n)

    myinnerfunc()
    print(n)
myfunc()
print(n)


# global --> It will change the value of the variable in the global scope.
# nonlocal --> It will change the value of the variable in the enclosing scope.