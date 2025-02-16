class Car:
    def __init__(self):
        self.brand = ""
        self.model = ""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __init__(self, brand = "BMW", model = "X5"):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand} - Model: {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car()

car1.display()