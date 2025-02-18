# Hierarchical

class Vehicle:
    def engine_type(self):
        print("Vehicle has an engine")

class Car(Vehicle):
    def num_doors(self):
        print("Car has 4 doors")


class Truck(Vehicle):
    def load_capicity(self):
        print("Truck can carry 10 tons")


car = Car()
car.engine_type()
car.num_doors()
truck = Truck()
truck.engine_type()
truck.load_capicity()

# Hybrid

class Shape:
    def area(self):
        print("Calculating area....")
    
class Polygon(Shape):
    def sides(self):
        print("Polygoan has multiple sides.")

class Rectangle(Polygon):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
    
    def area(self):
        return self.length * self.breath

rec = Rectangle(10, 5)
rec.sides()
print(rec.area())