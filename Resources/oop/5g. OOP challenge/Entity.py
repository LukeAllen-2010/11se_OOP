import random
from attacks import ATTACKS
from get_roll import get_roll


class Entity:
    def __init__(self, name:str, starting_health:int, player_attacks:list, armour_class:int, strength:int, dexterity:int, constitution:int=0, intelligence:int=0, wisdom:int=0, charisma:int=0, gp=0, sp=0, cp=0):
        self.name = name
        self.__health = starting_health
        self.abilities = {'strength':strength, 'dexterity':dexterity, 'constitution':constitution, 'intelligence':intelligence, 'wisdom':wisdom, 'charisma':charisma}
        self.purse = {'gold':gp, 'silver':sp, 'copper':cp}
        self.ac = armour_class
        self.attacks = {}
        for attack_name in player_attacks:
            self.attacks[attack_name] = ATTACKS[attack_name]

    def get_roll(self, dice_amount, dice_type):
        roll = 0
        for i in range(dice_amount):
            roll += random.randint(1, dice_type)
        return roll
    
    def get_ability_modifier(self, ability_type):
        return (self.abilities[ability_type] - 10) // 2
    
    def get_proficiency_bonus(self):
        return (self.level - 1) // 4 + 2
    
    def get_attack_roll(self, stat_bonus_modifier):
        return self.get_proficiency_bonus() + stat_bonus_modifier

    def attack_target(self, attack:str, target_ac):
        ability_bonus = self.attacks[attack]
        stat_bonus_modifier = self.get_ability_modifier(self.abilities[ability_bonus])
        if self.get_attack_roll() > target_ac:
            return bob.player_attacks[attack](stat_bonus_modifier)
        print(f'{self.name} MISSED!!')
        return 0

    def get_initiative_roll(self):
        return get_roll(1, 'd20') + self.get_ability_modifier('dexterity')

def get_roll(dice_amount, dice_type):
        roll = 0
        for dice in range(dice_amount):
            roll += DICE[dice_type]()
        return roll

bob = Entity('bob', 10, ['rend', 'halberd'], 10, 10, 10)

opps = {
    'jason' : Entity('jason', 10, ['rend'], 13, 14, 12),
    'monkey' : Entity('monkey', 5, ['rend', 'greatsword'], 10, 10, 10)
}

print(bob.attack_target('rend', 13))

print([1, 8, 4, 6, 3].sort())

initiative_order = {}

for opp in opps:
    initiative_order[opp] = opps[opp].get_initiative_roll()

print(initiative_order)
