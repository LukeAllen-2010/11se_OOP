import time
import random

def print_line(message, delay = 0.1):
    PAUSE = {'.' : 2, '?' : 3, '!' : 3, ',' : 1.5, ' ' : 0.25}
    for character in message:
        print(character, end='', flush=True)
        if character in PAUSE:
            time.sleep(delay*PAUSE[character])
        else:
            time.sleep(delay)


    # def add_attack(self, attack_name:str, dice_amount, dice_type, melee):
    #     if melee:
    #         ability_modifier = self.get_ability_modifier(self.abilities['strength'])
    #     else:
    #         ability_modifier = self.get_ability_modifier(self.abilities['dexterity'])
    #     self.attacks[attack_name] = Weapon(attack_name, dice_amount, dice_type, ability_modifier)


DICE = {
    'd4' : lambda : random.randint(1,4),
    'd8' : lambda : random.randint(1,8),
    'd10' : lambda : random.randint(1,10),
    'd12' : lambda : random.randint(1,12),
    'd20' : lambda : random.randint(1,20),
    'd100' : lambda : random.randint(0,99)
}

def get_roll(dice_amount, dice_type):
        roll = 0
        for dice in range(dice_amount):
            roll += DICE[dice_type]()
        return roll

class PhysicalAttack:
    def __init__(self, dice_amount, dice_type:str):
        self.DICE = (dice_amount, dice_type)
        # self.stat_bonus = stat_bonus
        # self.proficiency_bonus = proficiency_bonus
        # stat_bonus, proficiency_bonus,

    def get_dmg_roll(self, stat_bonus): # use get_roll and get_ability_score
        return get_roll(self.DICE[0], self.DICE[1]) + stat_bonus

strength = 3
proficiency_bonus = 2

attacks = {}

def add_attack(self, name, strength, proficiency_bonus):
    attacks[name] = PhysicalAttack(strength, proficiency_bonus, 1, 'd8')

class Entity:
    def __init__(self, name, attack_names:list):
        self.name = name
        self.player_attacks = {}
        for name_ in attack_names:
            self.player_attacks[name_] = ATTACKS[name_]

ATTACKS = {
    'rend' : PhysicalAttack(1, 'd4').get_dmg_roll, 
    'halberd' : PhysicalAttack(1, 'd10').get_dmg_roll, 
    'greatsword' : PhysicalAttack(2, 'd6').get_dmg_roll

    }

bob = Entity('bob', ['rend','halberd'])

print(bob.player_attacks['rend'](bob.strength))
print(bob.player_attacks['halberd'](bob.strength))


# Lightning Breath (Recharge 5–6). Dexterity Saving Throw: DC 15, each creature in a 60-foot-long, 5-foot-wide Line. Failure: 49 (9d10) Lightning damage. Success: Half damage.
# Repulsion Breath. Strength Saving Throw: DC 15, each creature in a 30-foot Cone. Failure: The target is pushed up to 40 feet straight away from the dragon and has the Prone condition.