# Association: is a relationship
class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop
    
    def show_laptop_info(self):
        print(f"{self.name} uses {self.laptop.brand}")

laptop = Laptop("Dell")
student = Student("John", laptop)

student.show_laptop_info()

# Aggregation: has a relationship
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        return [department.name for department in self.departments]

department1 = Department("Computer Science")
department2 = Department("Electrical Engineering")

university = University("XYZ University")

university.add_department(department1)
university.add_department(department2)

print(university.show_departments())

# Composition: part of relationship
class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)
    
    def show_car_info(self):
        print(f"{self.brand} car has {self.engine.power} power engine")
    
car = Car("Toyota", 1000)
car.show_car_info()
