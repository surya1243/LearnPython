#precedence hiararchy of operator
print(2+2*7/7)

#most of Python's operators have left-sided binding
print(9 % 6 % 2)

#but except for exponentiation, the exponentiation operator uses right-sided binding
print(2 ** 2 ** 3)

print((-2 / 4), (8 / 4), (2 // 4), (-2 // 4))

var = 1
print(var)
var = var + 1
print(var)

#Identity operators in Python
print("Identity operators in Python:")

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

#membership operators in Python
print("membership operators in Python:")
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)

print("id(x) = ", id(x))  #id is the built-in function to show the address of x in memory