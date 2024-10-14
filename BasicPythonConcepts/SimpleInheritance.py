class laptop:
    
    def __init__(self, batteryLife, screenSize):
        self.batteryLife = batteryLife
        self.screenSize = screenSize


class Windows(laptop):
    
    def __init__(self, batteryLife, screenSize, type):
        super().__init__(batteryLife, screenSize)
        self.type = type


class Mac(laptop):
    
    def __init__(self, batteryLife, screenSize, type):
        super().__init__(batteryLife, screenSize)
        self.type = type

        

x = Windows(100,1080,"gaming")
print(x.batteryLife)
print(x.screenSize)  
print(x.type)
y = Mac(100,2160,"productivity")
print(y.batteryLife)
print(y.screenSize)  
print(y.type)




# Extra parts for Classes

#hasattr () -> Used to check if the class has the attribute or not
print(hasattr(x,"batteryLife"))

#setattr() -> Used to set an attribute value 

setattr(x,"ChargingPort","Type-C")
print(hasattr(x,"ChargingPort"))