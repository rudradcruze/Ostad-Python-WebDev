a = [1, 2, 4, 5, 6, "a", 5, 6, 7, 8, 9, 10]

for item in a:
    if str(item).isnumeric():
        print(item)
    else:
        break

for item in a:
    if str(item).isnumeric():
        print(item)
    else:
        continue