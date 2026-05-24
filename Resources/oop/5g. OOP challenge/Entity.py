import random
from Hero import Attack

class Entity:
    def __init__(self, name:str, starting_health:int, weapon:str, armour_class:int, strength:int, dexterity:int, constitution:int, intelligence:int, wisdom:int, charisma:int, gp=0, sp=0, cp=0):
        self.name = name
        self.__health = starting_health
        self.weapon = Weapon()
        # self.weapon_name = weapon
        # self.weapon_dice = WEAPON_MAPPING[weapon]
        self.abilities = {'strength':strength, 'dexterity':dexterity, 'constitution':constitution, 'intelligence':intelligence, 'wisdom':wisdom, 'charisma':charisma}
        self.ac = armour_class
        self.attacks = {}

    def get_roll(self, dice_amount, dice_type):
        roll = 0
        for i in range(dice_amount):
            roll += random.randint(1, dice_type)
        return roll

    def add_attack(self, attack_name:str, dice_amount, dice_type, melee):
        if melee:
            ability_modifier = self.get_ability_modifier(self.abilities['strength'])
        else:
            ability_modifier = self.get_ability_modifier(self.abilities['dexterity'])
        self.attacks[attack_name] = Attack(attack_name, dice_amount, dice_type, ability_modifier)

    def get_ability_modifier(self, ability_score):
        return (ability_score - 10) // 2
    
    def get_proficiency_bonus(self):
        return (self.level - 1) // 4 + 2

