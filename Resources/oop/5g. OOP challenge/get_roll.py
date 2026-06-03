import random

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