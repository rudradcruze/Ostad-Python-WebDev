def check_file(file_name):
    if not file_name.endswith(".png"):
        raise ValueError("File must be a PNG")
    
try:
    check_file("data.csv")
except Exception as e:
    print("There was an error: ", e)