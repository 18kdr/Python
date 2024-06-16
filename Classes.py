class monster:
    health = 90
    energy = 70 
    
    def attack(self, attack):
        print(f"{attack} has been commeneced")
    
    def move(self, move):
        print(f"{move} has been destroyed")
        self.energy -= 20
        print(self.energy)

Monster = monster()

Monster.attack("attack")

Monster.move("left-wing")