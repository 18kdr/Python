# class Phone:
    
#     def __init__(self, batterySize, **kwargs):
#         self.batterySize = batterySize
#         super.__init__(**kwargs)

# class Apple:
#     def __init__(self, **kwargs):
#         self.kwargs = kwargs

# class Indian(Phone, Apple):
    
#     def __init__(self, variant, batterySize, screenSizeratio):
#         self.variant = variant
#         super.__init__(batterySize = batterySize, screenSizeratio = screenSizeratio)
    
    
# phone = Indian(variant = "Indian", batterySize = 100, screenSizeratio = "16:9")

# print(phone.batterySize)
# print(phone.variant)
# print(phone.kwargs)


class Apple:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        super().__init__(**kwargs)

class Phone:
    def __init__(self, batterySize, **kwargs):
        self.batterySize = batterySize
        super().__init__(**kwargs)

class Indian(Phone, Apple):
    def __init__(self, variant, batterySize, screenSizeratio):
        self.variant = variant
        super().__init__(batterySize=batterySize, screenSizeratio=screenSizeratio)

phone = Indian(variant="Indian", batterySize=100, screenSizeratio="16:9")

print(phone.batterySize)
print(phone.variant)
print(phone.kwargs)
