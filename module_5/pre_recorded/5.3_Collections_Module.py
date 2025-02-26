import collections


from collections import defaultdict as dct

# print(collections.__doc__)

# print(dir(collections))

fruits = ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

print(collections.Counter(fruits))
print(collections.Counter(fruits).most_common(2))

# word_dictonary = collections.defaultdict(list)
word_dictonary = dct(list)

word_dictonary['python'].append('a programming language')
word_dictonary['java'].append('another programming language')

print(word_dictonary)