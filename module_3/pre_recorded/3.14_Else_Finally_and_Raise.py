try:
    print("Hello")
    print(10/0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

file_name = "test.jpg"

def check_file(file_name):
    if not file_name.endswith(".png"):
        raise ValueError("File must be a PNG")

check_file(file_name)