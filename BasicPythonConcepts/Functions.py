# Sample Function 1 

def functionSample():
    result = "You are a failed person in the society"
    print(result)

def ParamFunction(name):
    print(f"Your name is {name}")

functionSample()

ParamFunction("Kartikay")

#  Excersize 1
def Calculator(num1,num2, operation):
    match operation:
        case "plus":
            print(f"Addition: {num1 + num2}")
        case "minus":
            print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    print(f"Division: {num1 / num2}")
    
    
Calculator(10,5,"minus")

# Excersize 2 

def Greeter(weekday, person = "Person", greet = "Hello"):
    print(f"{greet} {person}, It is  {weekday}")
    
Greeter("Monday", person= "Kartikay")

# Excersize 3 
# Arguments excersize
# pass " **kwargs for keyword arguments [Dictionary type output]"
def Sum(*args):
    # Using the built-in method
    print(sum(args))
    
    # Using the logical explanation method
    total = 0
    iteration = []
    for x in args:
        total += x
        iteration.append(x)
        
    print(total)
    print(iteration)

Sum(1,2,3,4,5)
Sum(0)


#Excersize 4 
# Scope Excersize

multiplier = 5
has_calculated = False

def multiply_calculator(number):
    global has_calculated
    result = number * multiplier
    has_calculated = True
    return result
    
print(multiply_calculator(6))
print(has_calculated)

# Factorial using functions
def len_func(my_number):
    factorial = 1
    for i in range(0,my_number):
        factorial =  factorial * (i + 1)
        print(factorial)

    
my_number = int(input("Enter the number you want to find factorial of :"))
len_func(my_number)

# Method 2 to write the factorial function with checks
def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    i = int(num)    
    while i > 1:
        i -= 1 
        num *= i
    return num

number = 5
print(factorial(number))


# Recursive Functions 

# Print the sum of all elements till the specified number 

def sum_func(my_num):
    if my_num == 1:
        return my_num 
    return my_num + sum_func(my_num - 1)
    
print(sum_func(7))

# Print the list at new line using recursion
def print_list(my_list = [], idx = 1):
    if idx == len(my_list):
        return 
    print(my_list[idx])
    print_list(my_list, idx + 1)
    
my_list = [1,2,3,4,4,55,56,7,8]
print_list(my_list,idx = 0)


#Lambda functions

simple_operation = lambda a,b:'hello' if a > b else "Hello"

print(simple_operation(2,5))