class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def move(self):
        print(f"{self.make} is moving")

    def stop(self):
        print(f"{self.make} is stopping")

    def turn(self):
        print(f"{self.make} is turning")

mycar = Car("Toyota", "Corolla", 2019)
mycar.move()
mycar.stop()
mycar.turn()