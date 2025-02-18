class Bike:
    def driver(self):
        return "Riding a bike"
    
class Car:
    def driver(self):
        return "Driving a car"

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "car":
            return Car()
        else:
            return ValueError("Invalid vehicle type")

vehicle = VehicleFactory.get_vehicle("bike")
print(vehicle.driver())
        