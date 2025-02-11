import os
import pathlib

if os.path.exists("name_2.txt"):
    print("File exists")
else:
    print("File does not exist")

file_path = pathlib.Path("name_2.txt")

if file_path.exists():
    print("File exists")
else:
    print("File does not exist")

print(os.path.abspath("name_2.txt"))
print(file_path.absolute())
print(file_path.is_file())
print(file_path.is_dir())
print(os.path.getsize("name_2.txt"))

with open("name_2.txt", 'r') as file:
    # print(file.tell())
    print(file.read(10))