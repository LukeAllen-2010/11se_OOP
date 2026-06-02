import random
from attacks import ATTACKS
from get_roll import get_roll


class Entity:
    def __init__(self, name:str, starting_health:int, player_attacks:list, armour_class:int, strength:int, dexterity:int, constitution:int=0, intelligence:int=0, wisdom:int=0, charisma:int=0, gp=0, sp=0, cp=0):
        self.name = name
        self.level = 1
        self.health = starting_health
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
    
    def get_attack_roll(self, ability_bonus_modifier):
        return self.get_proficiency_bonus() + ability_bonus_modifier

    def attack_target(self, attack:str, target_ac):
        ability_bonus_type = self.attacks[attack][1] # e.g dexterity or strength
        print(ability_bonus_type)
        print(self.abilities[ability_bonus_type])
        ability_bonus_modifier = self.get_ability_modifier(ability_bonus_type) # finding bonus by passing stat type into get_ability_modifier()
        if self.get_attack_roll(ability_bonus_modifier) > target_ac: 
            return self.attacks[attack][0]() # runs get_damage_roll() for that attack and returns number
        print(f'{self.name} MISSED!!')
        return 0

    def get_initiative_roll(self):
        return get_roll(1, 'd20') + self.get_ability_modifier('dexterity')

entities = {
    'jason' : Entity('jason', 10, ['rend'], 13, 14, 12),
    'monkey' : Entity('monkey', 5, ['rend', 'greatsword'], 10, 10, 10),
    'hero' : Entity('bob', 10, ['rend', 'halberd'], 10, 10, 10)
}

def get_initiative_order(entities):
    initiative_order = {}
    for entity in entities:
        initiative_order[entity] = entities[entity].get_initiative_roll()
    return {k : v for k, v in sorted(initiative_order.items(), key = lambda item : item[1])}

initiative_order = get_initiative_order()

running = True
while running:
    for entity in initiative_order:
        if entity == 'hero':
            

        if entity.is_dead:
            print(f'{entity.name} is dead')
            initiative_order.remove(entity)
        
        else:
            attack = entity.attack_target(random.choice(entity.attacks), entities['hero'].ac)
            entities['hero'].health -= attack
            if entities['hero'].health < 0:
                print('YOU LOSE')
                running = False
            
# enemies = ['troll_1', 'troll_2', 'goblin', 'bear', 'angry_toadstool']

# enemy_list_str = f'Which enemy would you like to hit: '
# for enemy_num, enemy in enumerate(enemies, 1):
#     enemy_list_str += f'{enemy}({enemy_num}) '

# player_target = int(input(enemy_list_str)) - 1
# # target = int(input(f'which enemy would you like to hit: {enemies[0]}(1), {enemies[1]}(2)'))
# player_target.get_roll(1,20)