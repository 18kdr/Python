#Excersize
print("If Loop")
money_available = 50

if money_available >= 80:
    print("Eat something Fancy")
elif money_available >= 45:
    print("Eat Something nice")
elif money_available >= 15:
    print("Eat something okay")
else:
    print("Eat something cheap")
    
    
#Complex if statement
#Excersize 1

money_available = 100
hungry = True
bored = True


if money_available >= 100 and hungry == True or bored == False:
    print("Eat something fancy")
    
#Excersize 2
print("If Loop")
if money_available >= 80:
    if hungry == True:
        if bored == True:
            print("Eat something Fancy")
            

#While Loop 
print("While Loop")
my_list = []
counter = 0
not_include = 58
while counter <= 100:
    if counter % 2 == 0 and counter != 58:
            my_list.append(counter)
    counter += 1
print(my_list)

# For Loop 

print("For Loop")   
practice_list = [[10,40,20,50],[2,42,10],[101,80,4]]
solution_list = []
for x in practice_list:
    for y in x:
        if y > 10: 
            if y > 100:
                break
            else:
                solution_list.append(y)

print(solution_list)

# Ternary If Example 
color = ""
x = 1
color='blue' if x > 5 else 'red'

print(color)