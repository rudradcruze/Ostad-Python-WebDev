try:
    fp = open("myfiles.txt", "r")
    content = fp.read()
    fp.close()
except FileNotFoundError as e:
    print("File not found")
    print(e)

print("This is the end of the program")