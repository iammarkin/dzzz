class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

car = Car("Mersedes", "GT63s ///AMG", 2023, 4)
print(f"Car: {car.make} {car.model} {car.year}, {car.num_doors} doors")

motorcycle = Motorcycle("Kawasaki", "Ninga", 2020, "310hp")
print(f"Motorcycle: {motorcycle.make} {motorcycle.model} {motorcycle.year}, {motorcycle.engine_size} engine size")