with open('name_2.txt', 'w') as file:
    file.write('Hello, World!')
    file.write('Hello, World!')
    file.write('Hello, World!')

with open('name_2.txt', 'w') as file:
    file.write('Hello there!')


with open('name_2.txt', 'a') as file:
    file.write('Hello there!\nwe are appending this text to the file')
    file.write('Hello there!\nwe are appending this text to the file')

lines = ['Hello there!\n', 'we are appending this text to the file\n']

with open('name_2.txt', 'a') as file:
    file.writelines(lines)
