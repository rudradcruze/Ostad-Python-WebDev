a = 5
b = 10

print("Initial values")
print("a =", a)
print("b =", b)

print("\nMethod 1")
# Swap the values of a and b
temp = a
a = b
b = temp

print("a =", a)
print("b =", b)

print("\nMethod 2")

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)