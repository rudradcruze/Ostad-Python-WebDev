fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

fruits = [fruits.capitalize() for fruits in fruits]

print(fruits)

li_len = [len(x) for x in fruits]
print(li_len)

cube_list = [x**3 for x in range(1, 11)]
print(cube_list)

cuble_list_odd = [x**3 for x in range(1, 11) if x % 2 != 0]
print(cuble_list_odd)