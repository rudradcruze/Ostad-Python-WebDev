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

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car()

print(car1.brand)
print(car1.model)

print(car2.brand)
print(car2.model)

print(car3.brand)
print(car3.model)