num_to_words = dict()

num_to_words[1] = "one"
num_to_words[2] = "two"
num_to_words[3] = "three"


print(num_to_words)

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}


if 'first_name' in person:
    print('Yes, first_name is in person', person['first_name'])
else:
    print('No, first_name is not in person')

print(person)
print(person['first_name'])

for item in num_to_words:
    print(item, num_to_words[item])

for key, value in person.items():
    print(key, value)

print(dir(person))

print(person.keys())
print(person.values())

print(num_to_words.items())