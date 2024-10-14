# Key Notes
# 1 -> Array in python does not Need to be homogenous in nature.

# Array declaration / Initialization
"""
array_1 = [1,"Kartikay",3,4,4,5]

print(array_1)
"""

# Create a one dimensional array 
"""
array_one = []
array_limit = int(input("Enter the maximum number of elements you want to enter:"))
varNew : int
for i in range(0,array_limit):
    varNew = int(input("Enter The Numbers:"))
    array_one.append(varNew)
maxTry : int = 5
    
searchNum = int(input("Enter the number you want to search:"))
if searchNum in array_one:
    print(searchNum,"is in the list.")
else:
    print("Number is not in the list.")
    
"""

# Two - dimensional array 
"""
rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of columns:"))
array_two = [[0 for x in range(cols)]for y in range(rows)]

element: int

for i in range(rows):
    for j in range(cols):
        print("Enter the element you want to enter at position:",j)
        element = int(input())
        array_two[i][j] = element
print(array_two)

searchNum = int(input("Enter the number you want to search:"))
found = False
for i in range(rows):
    for j in range(cols):
        if array_two[i][j] == searchNum:
            found = True
            print("Element is there in the matrix at:[{}][{}]".format(i,j))
            break
if not found:
    print("Number not in the list")
"""
# Search, Sort, Delete Operations in array
num = int(input("Enter the size of array:"))
array_three = []
for i in range(num):
    element = int(input("Enter your element"))
    array_three.append(element)
print(array_three)

# Searching Operation
searchNum = int(input("Enter the number you want to search"))
searchFlag = False
for i in range(len(array_three)):
    if searchNum == i:
        searchFlag = True
        print("The number is found at {}".format(i))
if not searchFlag:
    print("Number not found")

# Sorting Operation
array_three.sort()    
print(array_three)

# Delete Operation
deleteNum = int(input("Enter the number you wanna delete:"))
for i in range(len(array_three)):
    if i == deleteNum:
        array_three.remove(deleteNum)
        print("Element successfully removed")
print(array_three)