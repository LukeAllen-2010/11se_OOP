#Learning Intentions
#1. Make health private (it becomes __health)
#2. Use methods to check if the fighter object is dead

'''import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))



    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


you = Fighter('You',100,60,20)
troll = Fighter('Troll',200,30,10)

while True:
    you.defend(troll.random_attack)
    troll.defend(you.random_attack)'''

import random, time 

running = True

class Fighter:
    def __init__(self, name, strength, starting_health, weapon = None, shield_modifier = 0.1):
        self.name = name
        self.strength = strength
        self.weapon = weapon
        self.shield = 1 + shield_modifier
        self.__health = starting_health
    
    def get_weapon_dmg(self):
        if self.weapon == 'sword':
            return 10
        elif self.weapon == 'club':
            return 6
        elif self.weapon == 'halberd':
            return 8
        else:
            return 0

    def get_attack(self, target):
        if not self.block_attack(target):
            attack = self.strength + self.get_weapon_dmg() + random.randint(-5, 8)
            print(f'{self.name} does {attack} damage')
        else:
            attack = 0
        return attack
    
    def shield_successful(self, block_time, response, target):
        min = block_time / target.shield
        max = block_time * target.shield
        print(f'min: {min} | response: {response} | max: {max}')
        return min < response < max

    def block_attack(self, target):
        block_time = random.randint(1,3)
        input(f'{target.name}: Block in {block_time} seconds. Press enter when ready, then enter again for block')
        time_1 = time.time()
        input('')
        time_2 = time.time()
        time_passed = time_2 - time_1
        print('time_passed:', time_passed)
        if self.shield_successful(block_time, time_passed, target):
            print('Block successful')
            return True
        return False

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
        p2.set_health(p1.get_attack(p2))
    else:
        p1.set_health(p2.get_attack(p1))

bandit = Fighter('Benjamin', 7, 40, 'club')
hero = Fighter('Bartholemew the Worthy', 20, 100, 'sword', shield_modifier=0.3)

while running:
    fight(bandit, hero)
    print('======================\n')


