print('hello world')

#printing the expressions
print('*' * 10)

#Strings can be concatenated (glued together) with the + operator, and repeated with *
print(2 * 'pa' + 'ya')

#Python isinstance()
mystring = "hello"
myfloat = float(10)
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    
