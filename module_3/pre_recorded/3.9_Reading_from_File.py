# file = open('name.txt', 'r')
# content = file.read().strip()
# file.close()
# print(content)

with open('name.txt', 'r') as file:
    content = file.read().strip()

print(content)