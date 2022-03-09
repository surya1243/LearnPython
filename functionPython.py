def firstFunction(name):
    """The first line of a function is called the docstring, the return statement is optional."""
    print("My name is ", name)
    
    
myName = input("Tell me your name: ")
firstFunction(myName)
print(firstFunction.__doc__)  #printing of docstring


# next example with return statement
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))

# default argument  in python, we can have any number of arguments using the * sign - def greet(*message)

def greet(name, message="Good morning"):
    print("Hello, " + name + ' '+ message)
    
greet("surya")
greet("manoj", "Good afternoon")