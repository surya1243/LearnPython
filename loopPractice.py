#while loop_practice
#count the number of total Odd  and Even numbers

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
        print("the number %d is Odd number" %number)
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
        print("the number %d is Even number" %number)
        
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)