li = [1, 2, 3, 4, 323, 53, 623, 6336];

max_number = float('-inf')

for num in li:
    if num > max_number:
        max_number = num

print('Max number:', max_number)


min_number = float('inf')

for num in li:
    if num < min_number:
        min_number = num

print('Min number:', min_number)

sum = 0
for num in li:
    sum += num

print('Sum:', sum)