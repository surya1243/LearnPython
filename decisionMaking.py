num = 0.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
    
#nested if example
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
#if elif else statement practice
year = int(input("Enter a year: "))

if year> 1582:
    if year%4 != 0:
        print("its a common year")
    elif year %100 !=0:
        print ("its a leap year")
    elif year % 400 !=0:
        print("its common year")
    else:
        print("its a leap year")
else:
    print("Not within the gregorian calender")