# Base class for Vehicles
# Base Animal Class (Polymorphism Demonstration)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Specific Animal Classes
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Dog")
    
    def move(self):
        return f"{self.name} is running 🐕"

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, species="Bird")

    def move(self):
        return f"{self.name} is flying 🦅"

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, species="Fish")

    def move(self):
        return f"{self.name} is swimming 🐟"

# Base Vehicle Class (Polymorphism Demonstration)
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Specific Vehicle Classes
class Car(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color
    
    def move(self):
        return f"The {self.color} {self.make} {self.model} is driving 🚗"

class Plane(Vehicle):
    def __init__(self, make, model, engine_type):
        super().__init__(make, model)
        self.engine_type = engine_type
    
    def move(self):
        return f"The {self.make} {self.model} is flying with a {self.engine_type} engine ✈️"

class Boat(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def move(self):
        return f"The {self.make} {self.model} is sailing ⛵"

# Main Program to demonstrate polymorphism and inheritance
def demo_move():
    # Animals
    dog = Dog(name="Nevo")
    bird = Bird(name="Twinky")
    fish = Fish(name="Bibo")

    animals = [dog, bird, fish]

    for animal in animals:
        print(animal.move())  # Polymorphism in action

    print("\n")

    # Vehicles
    car = Car(make="Audi", model="Model A5", color="Black")
    plane = Plane(make="Boeing", model="777", engine_type="Jet")
    boat = Boat(make="Yamaha", model="242X", fuel_type="Gasoline")

    vehicles = [car, plane, boat]

    for vehicle in vehicles:
        print(vehicle.move())  # Polymorphism in action

if __name__ == "__main__":
    demo_move()
