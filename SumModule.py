class Sum:
    def __init__(self):
        pass
    # Sum function for addition of numbers
    def SumNew(self,numberOfInputs):
        new_empty_array = []
        for i in range(numberOfInputs):
            value = int(input(f"Enter number {i + 1}: "))
            new_empty_array.append(value)
        total_sum = sum(new_empty_array)
        print("The sum is:", total_sum)