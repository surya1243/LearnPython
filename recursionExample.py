def recurse(num):
    if num == 1:
        return 1
    else:
       return(num * recurse(num-1))
        
num=int(input("enter a number:"))

print("The factorial is : ", recurse(num) )