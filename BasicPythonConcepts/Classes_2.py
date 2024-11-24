# Practice class questions

'''class Student:
    average : int = 0
    def __init__(self,name,mark_1,mark_2,mark_3):
        self.name = name
        self.mark_1 = mark_1
        self.mark_2 = mark_2
        self.mark_3 = mark_3
    
    def Average_fn(self):
        average = (self.mark_1 + self.mark_2 + self.mark_3) / 3
        print(self.name)
        print(average)

student_1 = Student("Kartikay",80,85,90)
student_1.Average_fn()'''

# Practice class question_2
'''
class Bank:
    def __init__(self,bank_balance):
        self.bank_balance = bank_balance
        pass
    
    def credit(self,credit_amount):
        self.bank_balance += credit_amount
        print("Total Balance:",self.bank_balance)
        
    
    def debit(self,debit_amount):
        if self.bank_balance <= 5000:
            print("Not sufficient balance")
        else:
            self.bank_balance -= debit_amount
            print("Total Balance:",self.bank_balance)
        
    
    def showbalance(self):
        print("Total Balance:",self.bank_balance)

kartikay = Bank(10000)
kartikay.credit(1000)
kartikay.showbalance()
kartikay.debit(6000)
kartikay.showbalance
kartikay.debit(100)    
'''

# Practice question 3 

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
        pass
    def Area(self):
        area = self.pi * self.radius * self.radius
        print("Area of the circle:",area)
        pass
    def Perimeter(self):
        perimter = 2 * self.pi * self.radius
        print("Perimeter of the circle:",perimter)
        pass
    
    
circle_1 = Circle(5)
circle_1.Area()
circle_1.Perimeter()