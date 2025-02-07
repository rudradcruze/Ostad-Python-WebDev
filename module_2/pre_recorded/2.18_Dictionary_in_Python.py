a = {
    'Rudra' : 22,
    'Rohan' : 23,
    'Rahul' : 24,
    'Raj' : 25
}

print(a)
print(a.keys())
print(a.values())


for key in a:
    print(key)

for key in a.keys():
    print(key)

for value in a.values():
    print(value)

for key, value in a.items():
    print(key, value)

print(a.get('Rudra'))

a = [1, 2, 3]
b = ["Mango", "Apple", "Banana"]

c = dict(zip(a, b))
print(c)

print(c[1])