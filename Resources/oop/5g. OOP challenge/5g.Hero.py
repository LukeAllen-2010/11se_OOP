import random, time

WEAPON_MAPPING = {
    'dagger' : (1,4),
    'club' : (1,4),
    'spear' : (1,6),
    'greatsword' : (2,6),
    'halberd' : (1,10),
    'rapier' : (1,8)

}


class Hero:
    def __init__(self, name:str, starting_health:int, weapon:str, armour_class:int, strength:int, dexterity:int, constitution:int, intelligence:int, wisdom:int, charisma:int, gold=0, silver=0, copper=0):
        self.name = name
        self.__health = starting_health
        self.weapon_name = weapon
        self.weapon_dice = WEAPON_MAPPING[weapon]
        self.str = strength
        self.dex = dexterity
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma 
        self.ac = armour_class
        self.gp = gold
        self.sp = silver
        self.cp = copper
    
    def get_roll(self, dice_amount, dice_type):
        roll = 0
        for dice in range(dice_amount):
            roll += random.randint(1, dice_type)
        return roll
    
    def cast_spell(self):
        print('spell casted')

    def attack(self):
        player_input = input('What attack do you want to use? Cast spell (1), hit with weapon (2) or do a backflip (3)')
        x = getattr(self, player_input)
        try:
            x()
        except:
            print('Player input does not match attack options')



hero = Hero('Gimli', 100, 'halberd', 12, 10, 10, 10, 10, 10, 10)

# print(hero.get_roll(hero.weapon_dice[0], hero.weapon_dice[1]))
hero.attack()