# Learning intentions:
# - Create a protected attribute
# - Create a private attribute

class Pet():
    def __init__(self, name, category, breed):
        self.name = name
        self.__category = category
        self.__breed = breed
    
    def __str__(self):
        return f'Catgory: {self.__category}. Breed: {self.__breed}'

p1 = Pet('Benjamin', 'Monkey', 'Black Howler') 
print(p1)

#ACTIVITIES:
#1. Make category a private attribute than test to make sure it can't be changed once created
#2. Add another private attribute for breed