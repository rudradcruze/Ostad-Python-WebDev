def my_function(f_name, l_name, age):
    print(f"My name is {f_name} {l_name} and I am {age} years old.")

my_function(f_name = "John", age = 30, l_name = "Doe")

# Arbitrary Keyword Arguments, **kwargs

def marks(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    
marks(english = 90, bangla = 95, math = 85)