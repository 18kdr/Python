# Dictionaries

dict_1 = {'A':'Kartikay',
        'B':'Deep',
        'C':'Rane'}

print(dict_1.keys())
print(dict_1.values())

print(dict_1['A'])
print(dict_1.get('A'))


#Sets 
my_set = {1,1,1,4,5,3,2,2}

print(list(my_set)[1])

# Excersize : Find out the common elements in the list

set_1 = {6, 7, 3, 2.2, 5, 62, 2, 1, 3, 4, 5, 566, 3, 2, 34, 12}
set_2 = {3, 5, 34, 100, 200}

common_set = set_1 & set_2 
print(common_set)