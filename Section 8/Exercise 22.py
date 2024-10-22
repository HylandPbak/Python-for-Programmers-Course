#Tuples Exercise
#Because tuples can't be changed, I have started a function for you called appendtotuple(thetuple, value)

#Make it so that the function returns a new tuple that is a combination of thetuple and value at the end of that new tuple. Be sure that you are returning a tuple and not an array.

shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

def appendtotuple(thetuple, value):
    return thetuple + (value,)