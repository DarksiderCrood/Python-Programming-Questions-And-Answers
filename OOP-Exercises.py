# Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes
'''class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

model = Vehicle(240, 18)
print(model.max_speed, model.mileage)'''

# Exercise 2: Create a Vehicle class without any variables and methods
'''class NoVarMeth:
    pass'''

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
'''class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus_obj = Bus('Volvo', 210, 40)
print(bus_obj.name, bus_obj.max_speed, bus_obj.mileage)
'''
