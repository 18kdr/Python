# Sample class structure for creating class
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


#Excersise for creating a class
# My solution
class monster:
    def __init__(self, health):
        self.health = health

class hero:
    def attack(self, attack):
        monster1.health -= attack 

monster1 = monster(100)
print(monster1.health)

hero1 = hero()
hero1.attack(30)

print(monster1.health)

# Video Solution

class MonsterNew:
    def __init__(self, energy, healthNew):
        self.energy = energy
        self.healthNew = healthNew
    
    def get_damage(self, amountNew):
        self.healthNew -= amountNew
    
class HeroNew:
    def __init__(self, damageNew, monsterNew):
        self.damageNew = damageNew
        self.monster = monsterNew
        
    def attack(self):
        self.monster.get_damage(self.damageNew)   

monsterNew = MonsterNew(healthNew=100, energy=100)
heroNew = HeroNew(damageNew=20, monsterNew=monsterNew)

print(monsterNew.healthNew)  # Output initial health
heroNew.attack()
print(monsterNew.healthNew)  # Output health after attack






