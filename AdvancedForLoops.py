fruits = ["apple", "banana", "cherry", "date", "elderberry"]

numbers = [1, 2, 3, 4, 5]

colors = ["red", "blue", "green", "yellow", "purple"]

# Excersize:

# Solution_1
for x in enumerate(zip(fruits,numbers,colors)):
    print(f'ID:{x[0]} {x[1][0]} {x[1][2]} inventory: {x[1][1]}')

# Solution_2
for fruit,num,color in zip(fruits,numbers,colors):
    print(f'{fruit} {color} inventory: {num}')

