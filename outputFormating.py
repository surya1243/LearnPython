#sep and end output formatter
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

print("\n output formatter:")
x = 5; y = 10;
print('The value of x is {} and y is {}'.format(x,y))  #the curly braces {} are used as placeholders

print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'Surya'))

x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)  # %3.4f specified that the printed number should contain 4 digits after the decimal