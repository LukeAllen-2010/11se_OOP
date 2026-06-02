import random



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
    
    def get_attack_roll(self, attack:str, stat_bonus, target_ac):
        stat_bonus_modifier = self.get_ability_modifier(self.abilities[stat_bonus])
        if self.get_proficiency_bonus() + stat_bonus_modifier > target_ac:
            return bob.player_attacks[attack](stat_bonus_modifier)

    def get_initiative_roll(self):
        return get_roll(1, 'd20') + self.get_ability_modifier('dexterity')

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

ATTACKS = {
    'rend' : PhysicalAttack(1, 'd4').get_dmg_roll, 
    'halberd' : PhysicalAttack(1, 'd10').get_dmg_roll, 
    'greatsword' : PhysicalAttack(2, 'd6').get_dmg_roll

    }

bob = Entity('bob', ['rend','halberd'], )

opps = {
    'jason' : Entity('jason', 10, ['rend'], 13, 14, 12),
    'monkey' : Entity('monkey', 5, ['rend', 'dagger'], 10, 10, 10)
}

print(bob.player_attacks['rend'](bob.strength))
print(bob.player_attacks['halberd'](bob.strength))

print([1, 8, 4, 6, 3].sort())


