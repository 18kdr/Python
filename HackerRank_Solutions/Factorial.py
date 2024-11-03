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