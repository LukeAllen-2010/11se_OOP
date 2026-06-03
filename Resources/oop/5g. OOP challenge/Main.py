

# enemies[1]

import random, time

DICE = {
    'd4' : random.randint(1,4),
    'd8' : random.randint(1,8),
    'd10' : random.randint(1,10),
    'd12' : random.randint(1,12),
    'd20' : random.randint(1,20),
    'd100' : random.randint(0,99)
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
    def __init__(self, dice_amount, dice_type, ability_type, proficiency_bonus):
        self.d_amt = dice_amount
        self.d_type = dice_type
        self.ability_type = ability_type
        self.prof_bonus = proficiency_bonus

    def get_dmg_roll(self, roll, ability_modifier, attack_hits:bool): # use get_roll and get_ability_score
        if attack_hits:
            return roll + ability_modifier
        else:
            print('Attack misses')
            return 0


# class Humanoid(Entity):
#     def __init__(self, gold, silver, copper):
#         self.purse = {'gp':gold, 'sp':silver, 'cp':copper}