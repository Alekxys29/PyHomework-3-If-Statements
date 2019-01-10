"""
Homework Assignment #3: "If" Statements

This program accepts 3 parameters and checks for equality between any two of them.
The program returns True if 2 or more of the parameters are equal, and False if none 
of them are equal to any of the others.
"""
# Accepts 3 parameters and returns boolean result
def isEqual(param1, param2, param3):
    _var1 = int(param1)
    _var2 = int(param2)
    _var3 = int(param3)

    if _var1 == _var2 or _var1 == _var3 or _var2 == _var3:
        return True
    else:
        return False

# Assign the output of isEqual function to result varialble
result = isEqual("10",10,29)

# Print the result
print(result)