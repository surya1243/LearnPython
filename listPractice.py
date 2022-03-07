myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList[0])
print(myList[1])
print(myList[2])

#printing all the list elements
print("printing all the list elements of myList")
for x in myList:
    print(x)

print("The second element of the list is %d" % myList[1])
print("The first element of the list is", myList[0])

#using operator with a list
evenNumber = [2,4,6]
oddNumber = [1,3,5]
allNumbers = oddNumber + evenNumber

print(allNumbers)

