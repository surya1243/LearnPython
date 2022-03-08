# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
# Iterating over a sequence is called traversal.

#Syntax

# for val in sequence:
#    loop body

#val is the variable that takes the value of the item inside the the sequence on each iteration.

numberList = [1, 2, 3, 4, 5, 6, 7, 8]

sum =0

for val in numberList:
    sum+=val
    
print("the sum is: " , sum)


#program to display students marks from the record

studentName = "shankar"

marks = {"surya": 80, "manoj": 90, "shankar": 95}

for student in marks:
    if student == studentName:
        print("Marks scored by %s" % student + " is", marks[student])
        break
else:
    print("No student found")