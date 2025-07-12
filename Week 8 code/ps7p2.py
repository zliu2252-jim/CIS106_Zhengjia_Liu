# Define the object
class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def car_class(self):
        return self.make

    def car_model(self):
        return self.model

    def get_sticker_price(self):
        return self.sticker_price

    def discount_price(self):
        return 0.90 * self.sticker_price

# The derived class called Sport ('N' means not included)
class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = 'N'
        self.sport_engine = 'N'
        self.sport_interior = 'N'

    def SportWheels(self, include='Y'):
        self.sport_wheels = include

    def SportEngine(self, include='Y'):
        self.sport_engine = include

    def SportInterior(self, include='Y'):
        self.sport_interior = include

    def pricewithoptions(self):
        price = self.discount_price()
        if self.sport_wheels == 'Y':
            price += 1000.00
        if self.sport_engine == 'Y':
            price += 3000.00
        if self.sport_interior == 'Y':
            price += 2000.00
        return price

# Instantiate the object
car1 = Car('Toyota', 'Corolla', 30000.00)
sport1 = Sport('Tesla', 'Model-X', 50000.00)

# Use the object
print("Car make:", car1.car_class())
print("Car model:", car1.car_model())
print("Sticker price:", car1.get_sticker_price())
print("Discount price:", car1.discount_price())

print() # Blank line for separation

print("Car make:", sport1.car_class())
print("Car model:", sport1.car_model())
print("Sticker price:", sport1.get_sticker_price())
print("Discount price:", sport1.discount_price())

# Set the options about included or not included
sport1.SportWheels('Y')
sport1.SportEngine('Y')
sport1.SportInterior('Y')

print() # Blank line for separation

print("Price with options:", sport1.pricewithoptions())