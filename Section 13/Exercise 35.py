#Files - Reading and Writing
#I created a file for you called motto.txt. Read the file into exercise.py and print what was read in.

with open("motto.txt", "r") as file:
    content = file.read()
    print(content)