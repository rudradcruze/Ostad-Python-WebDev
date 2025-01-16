fruits1 = ['apple', 'banana', 'cherry']
fruits2 = ['date', 'elderberry']

# fruits1.extend(fruits2)

print(fruits1)

fruits1.insert(1, 'kiwi')

print(fruits1)

if 'apple' in fruits1:
    print('Yes, apple is in fruits1')
    print(fruits1.index('apple'))

fruits1.remove('banana')
print(fruits1)

# fruits1.remove('tamarind')
print(fruits1)

fruits1.pop(0)
print(fruits1)

list = [3, 8, 7, 9, 11]

# sort 
list.sort()
print(list)