class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name

class Father(GrandFather):
    def __init__(self, color, first_name, last_name):
        super().__init__(color, first_name)
        self.last_name = last_name

class Son(Father):
    def __init__(self, color, first_name, last_name, age):
        super().__init__(color, first_name, last_name)
        self.age = age
    
    def show_info(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and has {self.color} skin color")

son = Son("Brown", "John", "Doe", 25)
son.show_info()
