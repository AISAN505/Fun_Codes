import random
import os
#Creating Blueprint.
class Player:
    def __init__(self, hp:int , name:str , isBot: bool):
        self.hp = hp
        self.name = name
        self.isBot = isBot
        
    def attack_move(self):
        if self.isBot == True:
            index = random.randint(0,2)
            if index == 0:
                print(f"{self.name} chose 1st attack!")
            elif index == 1:
                print(f"{self.name} chose 2nd attack!")
            else:
                print(f"{self.name} chose 3rd attack!")
        else:
            index = int(input("choice an attack (0-2):"))
            if index == 0:
                print(f"{self.name} chose 1st attack!")
            elif index == 1:
                print(f"{self.name} chose 2nd attack!")
            else:
                print(f"{self.name} chose 3rd attack!")
# Creating the players                
human = Player(20, "Booker", True)
robot = Player(20, "Rekoob", False)

#Clear Screen 
def _cont():
    cont = input("")
    if cont == ":q":
        break
    
while True:
    os.system('clear')
    human.attack_move()
    _cont()
    robot.attack_move()
    
    
