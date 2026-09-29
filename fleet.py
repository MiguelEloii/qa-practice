def classify_speed(speed):
    if speed < 0:
        raise ValueError("Speed cannot be negative")
    if speed == 0:
        return "stopped"
    if speed < 120:
        return "normal"
    return "speeding"

class Vehicle:
    def __init__(self, plate, fuel_capacity=60):
        self.plate = plate
        self.fuel_capacity = fuel_capacity
        self.fuel = 0
        self.odometer = 0

    def refuel(self, liters):
        if liters <= 0:
            raise ValueError("Liters must be positive")
        if self.fuel + liters > self.fuel_capacity:
            raise ValueError("Tank capacity exceeded")
        self.fuel += liters

    def drive(self, km):
        if km <= 0:
            raise ValueError("Distance must be positive")
        fuel_needed = km / 10
        if fuel_needed > self.fuel:
            raise ValueError("Not enough fuel")
        self.fuel -= fuel_needed
        self.odometer += km