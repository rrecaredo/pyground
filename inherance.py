class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def abc(self):
        print("Car")

    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)


class Something:
    def abc(self):
        print("Something")

    def __init__(self, c):
        self.c = c


class Foobar(Car, Something):
    def __init__(self, make, color, model, doors, c):
        Car.__init__(self, make, color, model, doors)
        Something.__init__(self, c)

    def abc(self):
        print("Foobar")


obj1 = Foobar("Suzuki", "Grey", "2015", 4, 2)
obj1.printCarDetails()

super(Foobar, obj1).abc()
super(Car, obj1).abc()
