- define outside help
- How to create different attacks




TODO
- Make list of all attacks
- learn about kwargs: [w3schools](https://www.w3schools.com/python/python_args_kwargs.asp) and [geeksforgeeks](https://www.geeksforgeeks.org/python/args-kwargs-python/)

Attacks:
Dagger. Melee or Ranged Attack Roll: +4, reach 5 ft. or range 20/60 ft. Hit: 4 (1d4 + 2) Piercing damage.

Scimitar. Melee Attack Roll: +4, reach 5 ft. Hit: 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.

Shortbow. Ranged Attack Roll: +4, range 80/320 ft. Hit: 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

Rend. Melee Attack Roll: +7, reach 5 ft. Hit: 14 (2d8 + 5) Slashing damage.

#### Primeval Owlbear
Multiattack. The owlbear makes two Ravage attacks. ====

Ravage. Melee Attack Roll: +9, reach 5 ft. Hit: 15 (2d8 + 6) Slashing damage. If the target is a Huge or smaller creature and the owlbear moved 20+ feet straight toward it immediately before the hit, the target takes an extra 9 (2d8) Slashing damage and has the Prone condition.

Screech (Recharge 5–6). Constitution Saving Throw: DC 15, each creature in a 30-foot Emanation originating from the owlbear. Failure: 27 (6d8) Thunder damage, and the target has the Incapacitated condition until the end of its next turn. Success: Half damage only.

Lightning Breath (Recharge 5–6). Dexterity Saving Throw: DC 15, each creature in a 60-foot-long, 5-foot-wide Line. Failure: 49 (9d10) Lightning damage. Success: Half damage.

Repulsion Breath. Strength Saving Throw: DC 15, each creature in a 30-foot Cone. Failure: The target is pushed up to 40 feet straight away from the dragon and has the Prone condition.

### Notes:
- most attacks have an attack roll: d20 + proficienct bonus + stat and a damage roll: damage dice + stat
- some have bonuses for advanatge
- often have multiattack : make x attacks of y type
- Other attacks: 'stat' saving throw, else everyone in 'x' feet of 'distance_type' takes 'dice' damage 
    - distance_type: cone, line, circle, etc


PhysicalAttack

def phsycial_attack('name', )




## Story
- set in Swordcoast
- in a whole bunch of debt
- enslaved to Ironclad Syndicate guildmaster
- dungeoneering to pay off debts


## Room 
- enemy_count = int
- doors
    - doors = {door_number : randomly generated room?} 
    - or
    - 
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


class PhysicalAttack:
    def __init__(self, stat_bonus, proficiency_bonus, dice_amount, dice_type:str):
        self.DICE = (dice_amount, dice_type)

    def get_dmg_roll(self): # use get_roll and get_ability_score
        return get_roll(self.DICE[0], self.DICE[1])

rend = PhysicalAttack(strength, proficiency_bonus, 1, 8)

- attacks = {
    'rend' : rend, 
    'shortbow' : self.shortbow, 
    'dagger' : self.dagger
    }


<!-- - immunities = []? -->
<!-- - vulnerabilities = []? -->

- [get_roll](#get_roll)
- [get_attack_roll](#get_attack_roll)
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


### get_proficiency_bonus():
    BEGIN
        INPUT level # self
        bonus = (level - 1) // 4 + 2
        OUTPUT bonus
    END