a = [1, 2, 4, 5, 6, 7]

result = 0

i = 0
n = len(a)

while i < n:
    result += a[i]
    i += 1

print(result)

a = [-10, 2, 19, -3, -5]
print(a)

i = 0
while i < len(a):
    if a[i] < 0:
        a[i] = 0
    i += 1

print(a)