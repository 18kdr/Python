# This logic applies to print num, num -1 , num + 1 in one tuple 

# my_list = [(num-1 , num, num + 1) for num in range(0,99)]
# print(my_list)

# If the number is greater than 10 and only specifies the if condition

# my_list = [(num-1 , num, num + 1) for num in range(0,99)if num > 10]
# print(my_list)

# with else condition
my_list = [(num-1 , num, num + 1) if num > 10 else 0 for num in range(0,99)]
#print(my_list)

# Chess board excersize 

#My solution
chess_board_list = [[(f"{chr(y)}{x}") for x in range(1,9)] for y in range(ord('A'),ord('I'))]

for x in chess_board_list:
    print(x)

print("\n")
# Solution in video
chess_board_list_new = [[f"{y}{x}" for x in range(1,9)] for y in 'ABCDEFGH']

for x in chess_board_list_new:
    print(x)
    
#dict_comp
num = [1,2,3,4,5]
dict_comp = {letter : num for letter in 'ABCDEFGH'}

print(dict_comp)