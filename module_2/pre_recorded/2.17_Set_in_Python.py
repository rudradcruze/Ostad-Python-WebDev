# Set

a = [1, 2, 4, 4, 3, 3, 2, 2, 1, 1, 5, 6, 10]
s = set(a)
print(s)


a1 = {1, 3, 4, 5, 5}
b1 = {4, 5, 6, 7, 8, 10}

print(a1.union(b1))
print(a1.intersection(b1))
print(a1.difference(b1))

# Set Comprehension
c = {i**2 for i in range(10)}
print(c)