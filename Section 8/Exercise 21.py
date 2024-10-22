#Advanced Lists Exercise
#We're back at it again with the shoes list. I have provided you with the shoes list from the last exercise.

#In this exercise, I want you to make a function called addtofront, which will take in two parameters, a list and a value to add to the beginning of that list.

#Once you have made your function, add this line of code to your exercise:

#addtofront(shoes, "White Vans")

shoes = ["Spizikes","Air Force 1","Curry 2","Melo 5"]

def addtofront(lst, value):
    lst.insert(0, value) 


addtofront(shoes, "White Vans")