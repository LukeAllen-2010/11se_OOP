#Learning Intentions
#1. Create a Wizard class which inherits from a fighter
#2. Add a magic attribute 
#3. Modify the random attack method to include magic


import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name,':', 'Health:', str(self.__health))

    def is_dead(self):
        print(self.__health)
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))

        print(f'{self.name}\'s attack power: {attack_power}')
        return attack_power

    def skill_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
        target = random.randint(2,6)
        print('Hit enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: 
            multiplier = 0

        print(f'{self.name}\'s attack power: {attack_power}')
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')

    def roll_save(self):
        return random.randint(1,20)

    def get_health(self):
        return self.__health

class Spell:
    def __init__(self, name, damage, save_dc):
        self.name = str(name)
        self.damage = damage
        self.save_dc = save_dc
    
    def cast_check(self, save_attempt):
        if save_attempt < self.save_dc:
            return f'hit'
        else:
            return f'dodged'
        
    def cast_spell(self, save_attempt):
        if self.cast_check(save_attempt) == 'hit':
            attack = self.damage
        else:
            attack = 0
        return attack

global SPELL_MAPPING
SPELL_MAPPING = {
    1: "fireball", 
    2: "freeze",
    3: "eviscerate"
}

class Mage(Fighter):
    def __init__(self, name, starting_health, weapon, shield, proficiency_bonus):
        super().__init__(name, starting_health, weapon, shield)
        self.spells = {}
        self.prof_bonus = proficiency_bonus

    def add_spell(self, spell_name:str, spell_dmg:int, proficiency_bonus=0):
        self.spells[spell_name] = Spell(spell_name, spell_dmg, 8 + proficiency_bonus)

    def get_spell(self, spell_name):
        return self.spells[spell_name]

    def random_attack(self, save_attempt):
        action = input('What spell would you like to use: fireball (1), freeze(2) ')
        spell_name = SPELL_MAPPING[int(action)]
        spell = self.get_spell(spell_name)
        return spell.cast_spell(save_attempt)

hero = Mage('Gerald the Wise', 50, 6, 3, 3)
troll = Fighter('troll', 40, 10, 3)
entities = [hero, troll]
running = True

hero.add_spell('fireball', 20, hero.prof_bonus)
hero.add_spell('freeze', 15, hero.prof_bonus)

running = True

while running:
    if random.randint(1,2) == 1:
        hero.defend(troll.random_attack())
        troll.defend(hero.random_attack(troll.roll_save()))
    else:
        troll.defend(hero.random_attack(troll.roll_save()))
        hero.defend(troll.random_attack())

    print('=====================================================')

    if hero.is_dead():
        print('Thou hath perished, traveller. Thy journey comes to an end.')
    elif troll.is_dead():
        print('Congratulations, traveller. Thou hath slain thy enemy.')