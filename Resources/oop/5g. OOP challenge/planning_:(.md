## Story
- set in Swordcoast
- in a whole bunch of debt
- enslaved to Ironclad Syndicate guildmaster
- dungeoneering to pay off debts


## Room 
- enemy_count = int
- door_amount = int
- doors = [int] randomly chosen from other rooms
- [generate_room](#generate_room)





# CLASSES


## Spell
- name
- dmg_dice
- save_dc
- proficiency_bonus


## Entity
- stats = {} applied with standard array => split 6 random stats among your 
- name = str
- size = str (effects initial health calculation)
- armour_class = int
- weapon = instance of class Weapon
- attacks = []

<!-- - immunities = []? -->
<!-- - vulnerabilities = []? -->

- [get_roll](#get_roll)
- [get_ability_score](#get_ability_score)
- [get_proficiency_bonus](#get_proficiency_bonus)

### Hero(Entity)
- purse = {}
- race = str


### Monster(Entity)
- challenge_rating = float 
- attacks = []

- [add_attack](#add_attack)
self.add_attack(sword_attack(6))

## Attack
- damage_dice = (dice_amount, dice_type)
- melee = bool
- ranged = bool
- melee:strength, ranged:dexterity (when calculating bonuses for atk rolls)


- [get_attack_roll](#get_attack_roll)
- [get_damage_roll](#get_damage_roll)

### WeaponAttack(Attack)
- 

### UnarmedStrike(Attack)
d20 + strength mod + proficiency bonus
1 + strength mod
- self.name = name
- strength_mod = int
- damage
- proficiency_bonus

for bosses:
- lair actions (if boss)


MultiAttack
- attack = class # which attack is used
- attack_repeat = int # how many times attack is done





### generate_room():
    BEGIN
        INPUT enemies
        INPUT enemy_count
        FOR enemy = 1 TO enemy_count
            APPEND 
            
            
            enemies 

### generate_enemy():
    BEGIN
        enemy_list = [] # list





### get_attack_roll():
    BEGIN
        INPUT roll # get_roll
        INPUT proficiency_bonus
        INPUT stat_bonus # strength, dex, 
        INPUT target_ac
        if roll + proficiency_bonus + strength > target_ac
            OUPUT True
        OUPUT False
    END

### get_damage_roll():
    BEGIN
        INPUT roll # get_roll, using weapon dice
        INPUT bonus_modifier
        OUTPUT roll + bonus_modifier
    END


### get_roll(): 
    BEGIN 
        roll = 0
        INPUT DICE_TYPE
        FOR dice = 1 to DICE_TYPE
            roll = roll + random_integer(1, dice_type)
        NEXT dice
        OUTPUT roll
    END
    
### get_ability_score():
    BEGIN # get_ability_score
        INPUT ability_score
        stat_modifier = -5
        FOR score = 1 TO ability_score - 1
            stat_modifier = stat_modifier + 0.5
        NEXT score
        ROUND(score)
        INT(score)
        OUTPUT score
    END



### add_attack():
    BEGIN
        INPUT attack_name # e.g bite
        INPUT damage_dice # e.g 1d4 + strength
        INPUT strength OR dexterity
        INPUT melee or ranged
        {'melee' : 'strength', 'ranged' : 'dex'}
        IF melee IS True THEN
            ability_bonus = strength # self
        ELSE
            ability_bonus = dexterity # self
        END IF
        OUPUTE parent(attack_name, max_dmg) class


    - damage_dice = (dice_amount, dice_type)
- melee = bool
- ranged = bool
- melee:strength, ranged:dexterity (when calculating bonuses for atk rolls)


def add_spell(self, spell_name:strength, spell_dmg:int, proficiency_bonus=0):
    self.spells[spell_name] = Spell(spell_name, spell_dmg, 8 + proficiency_bonus)

### get_proficiency_bonus():
    BEGIN
        INPUT level # self
        bonus = (level - 1) // 4 + 2
        OUTPUT bonus
    END