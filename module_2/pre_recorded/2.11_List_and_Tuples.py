a = [1, 3, 4, 'Rudra', 'Rahul', 'Lira', 9.0, 5.3]

print(a[0])
print(a)

a[3] = 'Rahul'

print(a)
print(a[-1])

print(len(a))

s = 'He ll o world'

print(list(s))

a.append('Lira')

print(a)

a.append([1.4,23,654,234,5234])

print(a)
a.reverse()
print(a)


# Tuples

t = (1, 3, 4, 'Rudra', 'Rahul', 'Lira', 9.0, 5.3)
print(t)

print(t[5])

# t[3] = 'Rahul'

print(t)
t_r = tuple(reversed(t))
print(t_r)

