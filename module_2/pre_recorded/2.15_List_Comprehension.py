a = [10, 434, 45, 2345, 4234, 12, 656]

result =[]

for item in a:
    if item % 2 == 0:
        result.append(item)

print(result)

# List Comprehension
new_result = [item for item in a if item % 2 == 0]
print(new_result)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_new = [i**2 if i%2 == 0 else i for i in b]

print(b_new)