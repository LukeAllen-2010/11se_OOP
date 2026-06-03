# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets
pets = []

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
    def vaccinate(self):
        self.vaccinated = True


pets.append(Pet('Ben', 'monkey'))
pets.append(Pet('Jack', 'elephant'))
pets.append(Pet('Cupcake', 'taipan'))

for pet in pets:
    pet.vaccinate()
    print(pet.vaccinated)
#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list