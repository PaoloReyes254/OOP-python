class GeneralVehicle(object):
    def __init__(self, price, gas, color, miles):
        self.price = price
        self.gas = gas
        self.color = color 
        self.miles = miles
    
    def fill_tank(self):
        self.gas = 100

    def empty_tank(self):
        self.gas = 0

    def get_gas(self):
        return self.gas

    def get_price(self):
        return self.price

    def get_color(self):
        return self.color

    def paint(self, color):
        self.color = color

    def miles(self):
        return self.miles

class Car(GeneralVehicle):
    def __init__(self, price, gas, color, miles, doors):
        super().__init__(price, gas, color, miles)
        self.doors = doors

class Truck(GeneralVehicle):
    def __init__(self, price, gas, color, miles, load):
        super().__init__(price, gas, color, miles)
        self.load = load

class Motorcycle(GeneralVehicle):
    def __init__(self, price, gas, color, miles, tires):
        super().__init__(price, gas, color, miles)
        self.tires = tires

car1 = Car(10000, 83, "blue", 0, 4)
print(car1.get_color())
car1.paint("green")
print(car1.get_color())
print(car1.miles)
print(car1.get_price())
print(car1.get_gas())
car1.fill_tank()
print(car1.get_gas())
car1.empty_tank()
print(car1.get_gas())

print("")

truck1 = Truck(200000, 50, "red", 200, 2)
print(truck1.get_color())
truck1.paint("green")
print(truck1.get_color())
print(truck1.miles)
print(truck1.get_price())
print(truck1.get_gas())
truck1.fill_tank()
print(truck1.get_gas())
truck1.empty_tank()
print(truck1.get_gas())