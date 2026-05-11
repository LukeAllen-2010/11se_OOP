#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

class Fighter:
    def __init__(self, name, strength, weapon = None):
        self.name = name
        self.strength = strength
        self.weapon = weapon
        self.health = 100
    
    def get_weapon_damage(self):
        if self.weapon == 'sword':
            return 10
        elif self.weapon == 'club':
            return 6
        elif self.weapon == 'halberd':
            return 8

    def slime_out(self):
        attack = self.strength + self.get_weapon_damage + random.randint(-5, 8)
        return attack

player1 = Fighter('Benjamin', 4, 'club')
player2 = Fighter('Bartholemew the Worthy', 10, 'sword')

if random.randint(1, 2) == 1:
    player2.health -= player1.slime_out()
else:
    player1.health -= player2.slime_out()
