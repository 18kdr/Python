# How to open a file in python
# file = open('Booleans.py')
# print(file.read())
# file.close()

# This automatically closes the file
with open('Booleans.py', 'r') as file:
    print(file.read())