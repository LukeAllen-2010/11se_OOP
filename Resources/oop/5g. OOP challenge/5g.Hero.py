enemies = ['troll_1', 'troll_2', 'goblin', 'bear', 'angry_toadstool']

enemy_list_str = f'Which enemy would you like to hit: '
for enemy_num, enemy in enumerate(enemies, 1):
    enemy_list_str += f'{enemy}({enemy_num}) '

player_target = int(input(enemy_list_str))
# target = int(input(f'which enemy would you like to hit: {enemies[0]}(1), {enemies[1]}(2)'))
enemies[player_target - 1].shield

enemies[1]

import random, time

WEAPON_MAPPING = {
    'dagger' : (1,4),
    'club' : (1,4),
    'spear' : (1,6),
    'greatsword' : (2,6),
    'halberd' : (1,10),
    'rapier' : (1,8)

}

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

class Weapon:
    def __init__(self, dice_amount, dice_type, ability_type):
        self.d_amt = dice_amount
        self.d_type = dice_type
        self.ability_type = ability_type

class Hero:
    def __init__(self, name:str, starting_health:int, weapon:str, armour_class:int, strength:int, dexterity:int, constitution:int, intelligence:int, wisdom:int, charisma:int, gp=0, sp=0, cp=0):
        self.name = name
        self.__health = starting_health
        self.weapon_name = weapon
        self.weapon_dice = WEAPON_MAPPING[weapon]
        self.abilities = {'str':strength, 'dex':dexterity, 'con':constitution, 'int':intelligence, 'wis':wisdom, 'cha':charisma}
        self.ac = armour_class
        self.purse = {'gp':gp, 'sp':sp, 'cp':cp}

    def get_roll(self, dice_amount, dice_type):
        roll = 0
        for dice in range(dice_amount):
            roll += random.randint(1, dice_type)
        return roll

    def attack(self):
        player_input = input('What attack do you want to use? Cast spell (1), hit with weapon (2) or do a backflip (3)')
        x = getattr(self, player_input)
        try:
            x()
        except:
            print('Player input does not match attack options')

def get_ability_modifier(self, ability_score):
    ability_modifier = -5
    for score in range(ability_score):
        ability_modifier += 0.5
    return int(round(ability_modifier))


def get_dmg_roll(self, base_roll, ability_modifier): # use get_roll and get_ability_score
    if get_atk_roll():
        return base_roll + ability_modifier
    else:
        print('Attack misses')
        return 0
    

def get_atk_roll(self, target_ac):
    roll = self.get_roll(1, 20)
    proficiency_bonus = self.weapon.proficiency_bonus
    stat_bonus = 'str' #weapon's stat_bonue : str, dex, etc.
    ability_modifier = get_ability_modifier(self.ability[stat_bonus])
    if roll + proficiency_bonus + ability_modifier > target_ac:
        return True
    return False

def get_roll(self, d_amt, d_type):
    roll = 0
    for i in range(d_amt):
        roll += random.randint(1, d_type)
    return roll


hero = Hero('Gimli', 100, 'halberd', 12, 10, 10, 10, 10, 10, 10)

hero.attack()