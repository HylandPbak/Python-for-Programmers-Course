#Create a function called printtype that takes one parameter. If the parameter is a string, return "String"

#If the parameter is an int, return "Int"

#If the parameter is a float, return "Float"

def printtype(param):
    if isinstance(param, str):
        return "String"
    elif isinstance(param, int):
        return "Int"
    elif isinstance(param, float):
        return "Float"
    else:
        return "Unknown type"
