#Implicit and explicit Type conversion

anything = int(input("Enter the number: "))  #explicit Type conversion of string to int
something = anything ** 2.0
print(anything, "to the power of 2 is ", something)

print(type(something))
print(type(anything))

firstNumber = 6
secondNumber = 3.0
sum = firstNumber + secondNumber
print(sum)
print("The data type of sum is ", type(sum))
strSum = str(sum)           #explicit Type conversion of float to string
print("The data type of sum is ", type(strSum))
