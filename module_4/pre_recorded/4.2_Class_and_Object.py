class Car:
    def __init__(self):
        self.brand = "Toyota"
        self.model = "Corolla"

car1 = Car()
car1.brand = "Honda"
car1.model = "Civic"

print(car1.brand)
print(car1.model)