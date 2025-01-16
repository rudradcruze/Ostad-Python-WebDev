with open("myfile.txt", "r") as fp:
    # content = fp.readlines()
    # content = fp.readline()
    content = fp.read()
    print(content)