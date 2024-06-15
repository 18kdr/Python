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