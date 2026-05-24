import random
from Main import Weapon
class Entity:
    def __init__(self, name:str, starting_health:int, weapon:str, armour_class:int, strength:int, dexterity:int, constitution:int, intelligence:int, wisdom:int, charisma:int, gp=0, sp=0, cp=0):
        self.name = name
        self.__health = starting_health
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
        self.attacks[attack_name] = Weapon(attack_name, dice_amount, dice_type, ability_modifier)

    def get_ability_modifier(self, ability_score):
        return (ability_score - 10) // 2
    
    def get_proficiency_bonus(self):
        return (self.level - 1) // 4 + 2
    
WEAPON_MAPPING = {
    'dagger' : (1,4),
    'club' : (1,4),
    'spear' : (1,6),
    'greatsword' : (2,6),
    'halberd' : (1,10),
    'rapier' : (1,8)
}

hero = Entity('Gimli', 100, 'halberd', 12, 10, 10, 10, 10, 10, 10)
hero.add_attack('Halberd', WEAPON_MAPPING['halberd'][0], WEAPON_MAPPING['halberd'][1], True)


print(hero.attacks)

