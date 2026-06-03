from get_roll import get_roll

class PhysicalAttack:
    def __init__(self, dice_amount, dice_type:str):
        self.DICE = (dice_amount, dice_type)

    def get_dmg_roll(self, ability_bonus): # use get_roll and get_ability_score
        return get_roll(self.DICE[0], self.DICE[1]) + ability_bonus
    
ATTACKS = {
    'rend' : (PhysicalAttack(1, 'd4').get_dmg_roll, 'strength'), 
    'halberd' : (PhysicalAttack(1, 'd10').get_dmg_roll, 'strength'), 
    'greatsword' : (PhysicalAttack(2, 'd6').get_dmg_roll, 'strength'),
    'rapier' : (PhysicalAttack(1, 'd8'), 'dexterity'),
    'shortbow' : (PhysicalAttack(1, 'd6'), 'dexterity')
}