#Conditionals Exercise
#Make an if-else statement where if year is between 2000 and 2100 then print out:

#Welcome to the 21st century!

#Else print out:

#You are before or after the 21st century

year = 1830 

message = ""
if 2000 <= year <= 2100:
    message = "Welcome to the 21st century!"
else:
    message = "You are before or after the 21st century"
    
print(message)