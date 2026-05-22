class structure:
- instance variable / attribute
> function

<details>
    <summary>Weapon</summary>

- dice_amt # 3 in 3d6 (amount of dice being rolled)
- dice_type # 6 in 3d6 (type of dice being rolled)
- melee/ranged = boolean #? e.g ranged = False (thus melee is true)
melee-strength, ranged-dex

- cost?
- finesse? = boolean #Can use either dex or str

> get_atk_roll():

    BEGIN
        INPUT roll # get_roll
        INPUT proficiency_bonus
        INPUT stat_bonus # str, dex, 
        INPUT target_ac
        if roll + proficiency_bonus + strength > target_ac
            OUPUT True
        OUPUT False
    END

> get_dmg_roll():

    BEGIN
        INPUT roll # get_roll, using weapon dice
        INPUT bonus_modifier
        OUTPUT roll + bonus_modifier
    END



> get_dmg_roll
</details>  


<details>
<summary>Spell</summary>

</details>


Entity
- stats = {}
- name = str
- size = str (effects initial health calculation)
- armour_class



Humanoid(Entity)
- purse = {}
- weapon # using class weapon


Goblinoid(Entity)



    __init__ (needs name, weapon, ac, stats and money)

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

===


===


====

    BEGIN #get_roll()
        roll = 0
        INPUT DICE_TYPE
        FOR dice = 1 to DICE_TYPE
            roll = roll + random_integer(1, dice_type)
        NEXT dice
        OUTPUT roll
    END

    def roll_to_hit()
        

    def basic attack(self):
        










class Mage(Hero):
    def __init__(self, name, starting_health, weapon, shield, proficiency_bonus):
        super().__init__(name, starting_health, weapon, shield)
        self.spells = {}
        self.prof_bonus = proficiency_bonus

    def add_spell(self, spell_name:str, spell_dmg:int, proficiency_bonus=0):
        self.spells[spell_name] = Spell(spell_name, spell_dmg, 8 + proficiency_bonus)

    def get_spell(self, spell_name):
        return self.spells[spell_name]

    def cast_spell(self, save_attempt):
        action = input('What spell would you like to use: fireball (1), freeze(2) ')
        spell_name = SPELL_MAPPING[int(action)]
        spell = self.get_spell(spell_name)
        return spell.cast_spell(save_attempt)





    
    