# fp = open('myfile.txt', 'w')

# lines = ['Apple\n', 'Banana\n', 'Cherry\n', 'Date\n']
# # fp.write('Hello, World!')
# fp.writelines(lines)

fp = open('myfile.txt', 'a')

lines = ['Apple\n', 'Banana\n', 'Cherry\n', 'Date\n']
fp.writelines(lines)

# content = fp.read()
# print(content)

fp.close()