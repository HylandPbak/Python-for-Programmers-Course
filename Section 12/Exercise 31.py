#Method Exercise
#Add a method to the Car class called age that returns how old the car is (2016 - year)

class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def age(self):
        return 2016 - self.year