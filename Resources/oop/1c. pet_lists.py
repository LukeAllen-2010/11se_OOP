#Tutorial 3 Lists:
#1. Create an example of parallel lists eg: pet_name, species, age, vaccination_status for three pets
pets = []
pets.append(['Bonnie', 'cat', 3, False])
pets.append(['Ben', 'monkey', 25, False])
pets.append(['Luke', 'dog', 15, True])

#2. Use a for loop to print parallel list details. This will mean that one complete printout will look like:
'''
Pet name: Foxy
Species: Dog
Age: 8
Vaccination Status: False
'''

def print_pets(list):
  for pet in pets:
      print(f'Pet name: {pet[0]}\nSpecies: {pet[1]}\nAge: {pet[2]}\nVaccination States: {pet[3]}')
      print(' ')

def print_pets(list):
  for pet in pets:
      print(f'Pet name: {pet[0]}\nSpecies: {pet[1]}\nAge: {pet[2]}\nVaccination States: {pet[3]}')
      print(' ')
#3. Demonstrate what happens when an item is deleted

pets.remove(pets[2])
print_pets(pets)
pets.remove(pets[2])
print_pets(pets)


  #ACTIVITIES:
# In each activity test out that the printing of data is still valid
#1. Add a new animal named Hootie, its a blowfish, it is 34 years
pets.append(['Hootie', 'blowfish', 34, False])

#2. Vaccinate an unvaccinated animal (create vaccination)
def vaccinate(pet):
   pet[3] = True

vaccinate(pets[2])
#3. Remove an animal and make sure that all the printing is correct
def remove_pet(list, pet_number):
  pets.remove(list[pet_number])

remove_pet(pets, 2)
print(pets)