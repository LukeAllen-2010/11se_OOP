#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

running = True

class Fighter:
    def __init__(self, name, strength, weapon = None):
        self.name = name
        self.strength = strength
        self.weapon = weapon
        self.__health = 100
    
    def get_weapon_dmg(self):
        if self.weapon == 'sword':
            return 10
        elif self.weapon == 'club':
            return 6
        elif self.weapon == 'halberd':
            return 8
        else:
            return 0

    def get_attack(self):
        attack = self.strength + self.get_weapon_dmg() + random.randint(-5, 8)
        print(f'{self.name} does {attack} damage')
        return attack
    
    def set_health(self, modifier):
        self.__health -= modifier
        if self.__health <= 0:
            self.is_dead()

    def is_dead(self):
        global running
        running = False
        print(self.name, 'loses')
    
def fight(p1, p2):
    if random.randint(1, 2) == 1:
        p2.set_health(p1.get_attack())
    else:
        p1.set_health(p2.get_attack())

player1 = Fighter('Benjamin', 4, 'club')
player2 = Fighter('Bartholemew the Worthy', 10, 'sword')

while running:
    fight(player1, player2)