from attacks import ATTACKS
from get_roll import get_roll
import random

class Entity:
    def __init__(self, name:str, starting_health:int, player_attacks:list, armour_class:int, strength:int, dexterity:int, constitution:int=0, intelligence:int=0, wisdom:int=0, charisma:int=0, gp=0, sp=0, cp=0):
        self.name = name
        self.level = 1
        self.health = starting_health
        self.abilities = {'strength':strength, 'dexterity':dexterity, 'constitution':constitution, 'intelligence':intelligence, 'wisdom':wisdom, 'charisma':charisma}
        self.ac = armour_class
        self.attacks = {}
        for attack_name in player_attacks:
            self.attacks[attack_name] = ATTACKS[attack_name]
    
    def get_ability_modifier(self, ability_type):
        return (self.abilities[ability_type] - 10) // 2
    
    def get_proficiency_bonus(self):
        return (self.level - 1) // 4 + 2
    
    def get_attack_roll(self, ability_bonus_modifier):
        return get_roll(1, 'd20') + self.get_proficiency_bonus() + ability_bonus_modifier

    def attack_target(self, attack:str, target_ac):
        ability_bonus_type = self.attacks[attack][1] # e.g dexterity or strength
        print(f'{ability_bonus_type}: {self.abilities[ability_bonus_type]}')
        ability_bonus_modifier = self.get_ability_modifier(ability_bonus_type) # finding bonus by passing stat type into get_ability_modifier()
        roll = self.get_attack_roll(ability_bonus_modifier)
        print(roll)
        if roll > target_ac:
            print(f'{self.name} HIT!!!')
            return self.attacks[attack][0](ability_bonus_modifier) # runs get_damage_roll() for that attack and returns number
        print(f'{self.name} MISSED!!')
        return 0

    def get_initiative_roll(self):
        return get_roll(1, 'd20') + self.get_ability_modifier('dexterity')
    
    def is_dead(self):
        return self.health <= 0
    
    def choose_attack(self):
        print('These are your attacks: ', end='', flush=True)
        for attack in self.attacks:  
            print(f'{attack}, ')
        return input('which do you pick?\n').lower()


class Monster(Entity):
    def __init__(self, name, starting_health, player_attacks, armour_class, strength, dexterity, constitution = 0, intelligence = 0, wisdom = 0, charisma = 0):
        super().__init__(name, starting_health, player_attacks, armour_class, strength, dexterity, constitution, intelligence, wisdom, charisma)

    def get_turn(self, target):
        attack = self.attack_target(random.choice(list(self.attacks)), target.ac)
        return attack


            # if hero.is_dead():
            #     print('\nYOU LOSE!\n')
            #     running = False
            #     break
            # else:
            #     print(f'{hero.name} still alive at {hero.health}HP')