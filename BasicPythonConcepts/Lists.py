#Mutable
kartikay_list = [1,8,3,4,5,6]
#Immutable
kartikay_newList = [1,2,3,4,5,6,7,8,9,10]

print(len(kartikay_list))



kartikay_list.append(7)

print(kartikay_list)

kartikay_list.sort()

print(kartikay_list[2])
print(kartikay_list)
print(kartikay_list[0:])
print(kartikay_list[4:2:-1])
print(kartikay_list[4:6:1])
#List Excersize - 1
exercize_list = ['first entry', [123,456,[0,'Hello :)']],'bye'] 
print(exercize_list[1][2][1])

#List Excersize - 2

print(kartikay_newList[7:0:-2])
print(kartikay_newList)


#Unpacking the value 

value_1 = 2
value_2 = 3
print(value_1,value_2)
value_1, value_2 = 3,2
print(value_1,value_2)


# String manipulation

var_1 = "This is a good python course"
print(list(var_1))
var_2,var_3,var_4,var_5,var_6 = "This","is","an", "good","python course"
print(" ".join([var_2,var_3,var_4,var_5,var_6]))


list_new = [3,5,6,7,8,9]

print(str(list_new).strip('[]').replace(',',""))