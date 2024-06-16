#Exercise

inventory_names = ["Screwww","Wheelsss","Tires"]
inventory_numbers = [55,12,44]
inventory = list(zip(inventory_names, inventory_numbers)) 

# Zipped inventory
print(inventory)

#Solution to sort the array based on the number in the list
print(sorted(inventory,key = lambda item: item[1]))

# Solution to sort the function acording to the len of the name
print(sorted(inventory,key = lambda item: len(item[0])))

my_list = [1,2,3,4,5,6,7,8]
my_list_new = []

# Filter function in video solution
print(list(filter(lambda num : num > 4, my_list)))

# Filter function made simple
for i in range(len(my_list)):
    if my_list[i] > 4:
        my_list_new.append(my_list[i])

print(my_list_new)



# Excersize
# Converting both into list comrehension ( filter, map)

my_list_comprehension = [( i ** 2)  for i in range(len(my_list)) if i > 4]

print(my_list_comprehension)