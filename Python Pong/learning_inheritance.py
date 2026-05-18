class Hero: # PARENT CLASS
    def __init__(self, character_name, strength, skill_proficiency):
        self.name = character_name
        self.strength = strength
        self.proficiency = skill_proficiency
        self.alive = True
        self.languages = []
    
    def print_info(self):
        print(f'Name: {self.name}\nStrength:{self.strength}\nSkill_proficiency: {self.proficiency}')
        print(self)

class Fighter(Hero):
    def __init__(self, character_name, strength, skill_proficiency, weapon):
        super().__init__(character_name, strength, skill_proficiency) # Grabs the values from parent class
        self.type = 'fighter'
        self.weapon = weapon

class Wizard(Hero):
    def __init__(self, character_name, strength, magic_type):
        super().__init__(character_name, strength, skill_proficiency) # Grabs the values from parent class
        self.type = 'wizard'
        self.mag_type = magic_type

class Rogue(Hero):
    def __init__(self, character_name, strength):
        super().__init__(character_name, strength, skill_proficiency) # Grabs the values from parent class
        self.type = 'rogue'
        self.languages.append('Thieves Cant')
    

hero_name = input('Hello traveller. What is your name? ')
class_choice = input('Choose a class: Fighter, Wizard or Rogue. ').lower()

if class_choice == 'fighter':
    skill_proficiency = input('What skill would you like proficiency in: \'Athletics\' or \'Intimidation\': ')
    weapon = input('What weapon do you use? ')
    hero = Fighter(hero_name, 20, skill_proficiency, weapon)

elif class_choice == 'wizard':
    skill_proficiency = input('What skill would you like proficiency in: \'Arcana\' or \'History\': ')
    hero = Wizard(hero_name, 5, skill_proficiency, input('What school of magic have you chosen? '))

elif class_choice == 'rogue':
    skill_proficiency = input('What skill would you like proficiency in: \'Sleight of Hand\' or \'Stealth\': ')
    hero = Rogue(hero_name, 15, skill_proficiency)

else:
    raise NameError("Incorrect input. Must input offered options")

hero.print_info()