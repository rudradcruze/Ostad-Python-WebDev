li = [1, 3, 6, 232, 535, 12, 5354, 44]

print(li.index(6))

found = 5 in li
print(found)

found = 12 in li
print(found)

search = 555

flag = False
for i in range(len(li)):
    if li[i] == search:
        print('Found at index:', i)
        flag = True
        break

if not flag:
    print('Not found')