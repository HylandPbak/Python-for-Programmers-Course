#Init Exercise
#Add an init function to the Car class that takes the parameters year, make and model. Make all of these instance variables.

class Car:
    definition = "Something with 4 wheels and an engine"
    
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
