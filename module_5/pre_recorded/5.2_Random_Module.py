import random

# help(random)
# print(dir(random))
# print(random.__doc__)
print(random.random())
print(random.uniform(5, 10))
print(random.randint(5, 10))
print(random.randrange(5, 10, 2))


fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)

def generate_pin():
    return random.choice(range(1000, 10000))

print(generate_pin())