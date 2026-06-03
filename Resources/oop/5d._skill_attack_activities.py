#Learning Intentions
#1. Create a skill attack method
#2. Use the time library to set up a timing measure (skill factor)
#3. Have the skill increase or decrease the final attack value

import random, time 

'''class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')

'''
running = True

class Fighter:
    def __init__(self, name, strength, starting_health, shield = 0, weapon = None, skill_name = None, skill_dmg = 0, skill_time_modifier = 0.04):
        self.name = name
        self.strength = strength
        self.weapon = weapon
        self.skill_time_range = 1 + skill_time_modifier
        self.__health = starting_health
        self.skill = skill_name
        self.skill_dmg = skill_dmg
        self.shield = shield
    
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
        attack = self.strength + self.get_weapon_dmg() + random.randint(-3, 4)
        if self.use_skill():
            print(f'{self.name} uses {self.skill}')
            attack += self.skill_dmg
        else:
            print('skill failed (you suck)')
        return attack
    
    def skill_successful(self, skill_time, response):
        min = skill_time / self.skill_time_range
        max = skill_time * self.skill_time_range
        print(f'min: {min} | response: {response} | max: {max}')
        return min < response < max

    def use_skill(self):
        if not self.skill == None:
            skill_time = random.randint(1,3)
            input(f'{self.name}: Cast in {skill_time} seconds. Press enter when ready, then enter again for block')
            time_1 = time.time()
            input('')
            time_2 = time.time()
            time_passed = time_2 - time_1
            if self.skill_successful(skill_time, time_passed):
                print('Block successful')
                return True
            return False
        
    def defend(self, attack):
        print('Attack:', attack)
        print(f'Shield: {self.shield}')
        damage = attack - self.shield
        if damage >  0:
            self.set_health(damage)
        else:
            print(f'{self.name} fully blocked the attack')
            damage = 0

    def set_health(self, modifier):
        print(f'{self.name} takes {modifier} damage')
        self.__health -= modifier
        if self.__health <= 0:
            self.is_dead()

    def is_dead(self):
        print(self.name, 'loses ⚔️ ⚔️')
        global running
        running = False
    
def fight(p1, p2):
    if random.randint(1, 2) == 1:
        p2.defend(p1.get_attack())
    else:
        p1.defend(p2.get_attack())

bandit = Fighter('Benjamin', 7, 40, weapon='club', skill_name='kick', skill_dmg=5, skill_time_modifier=0.1)
hero = Fighter('Bartholemew the Worthy', 16, 100, weapon='sword', shield=13, skill_name = 'Divine Smite', skill_dmg=29, skill_time_modifier=0.07)

while running:
    fight(bandit, hero)
    print('=========================================')