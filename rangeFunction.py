# range() function can generate a sequence of numbers. range(10) will generate numbers from 0 to 9.
# We can also define the start, stop and step size as range(start, stop,step_size).

print(range(10))
print(list(range(20)))
print(list(range(5, 10)))
print(list(range(3, 20, 2)))

#program to iterate through a list using indexing

car = ['maruti', 'tesla', 'BMW']

for i in range(len(car)):
    print("I like", car[i])
