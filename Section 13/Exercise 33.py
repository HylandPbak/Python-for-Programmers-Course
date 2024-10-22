#None Exercise
#Create a function called square that takes in a number and returns the square of that number. If what's passed in is not a float or an int, return None

def square(number):
    if isinstance(number, (int, float)):
        return number ** 2
    else:
        return None