from functools import reduce

# Anonymous function: A function that is defined without a name.

# Syntax: lambda arguments: expression

def square(x):
    return x * x

print(square(5))  # 25

square_lambda = lambda x: x * x

print(square_lambda(4))

add = lambda a, b: a + b

students = [('Rudra', 90), ('John', 56), ('Doe', 80)]
sorted_students = sorted(students, key = lambda x: x[1])

print(sorted_students)

print(add(5, 6))

# map(), filter(), reduce()

# map

numbers = [1, 2, 3, 4, 5]

sq_numbers = list(map(str, numbers))
sq_numbers = list(map(float, numbers))
sq_numbers = list(map(lambda x: x * x, numbers))
print(sq_numbers)

# filter
even = map(lambda x: x % 2 == 0, numbers)
print(list(even))

even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))

# reduce

sum = reduce(lambda a, b: a + b, numbers)
print(sum)