class PhysicalAttack:
    def __init__(self, dice_amount, dice_type:str):
        self.DICE = (dice_amount, dice_type)

    def get_dmg_roll(self, stat_bonus): # use get_roll and get_ability_score
        return get_roll(self.DICE[0], self.DICE[1]) + stat_bonus
    
ATTACKS = {
    'rend' : PhysicalAttack(1, 'd4').get_dmg_roll, 
    'halberd' : PhysicalAttack(1, 'd10').get_dmg_roll, 
    'greatsword' : PhysicalAttack(2, 'd6').get_dmg_roll
}