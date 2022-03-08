print("Tell me your name:")
name = input()
print("hey", name)

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# Testing TypeError message.

anything = input("Enter a number: ")
something = anything ** 2.0  #probhited operation because, the result of input() function is string
print(anything, "to the power of 2 is", something)
