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

# Lightning Breath (Recharge 5–6). Dexterity Saving Throw: DC 15, each creature in a 60-foot-long, 5-foot-wide Line. Failure: 49 (9d10) Lightning damage. Success: Half damage.
# Repulsion Breath. Strength Saving Throw: DC 15, each creature in a 30-foot Cone. Failure: The target is pushed up to 40 feet straight away from the dragon and has the Prone condition.