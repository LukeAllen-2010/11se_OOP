#Tutorial 4 Dictionaries
#1 Create a Dictionary that stores pet information
#2 Change values within the dictionary
#3 Add values to the dictionary

pet1 = {
'name' : 'Bonnie',
'animal category' : 'Cat',
'age' : 3,
'vaccinated' : True,
'credit card' : '3423 2326 7543 1234',
'billing address' : '17 Park Drive, The Shire 3695',
'owner name' : 'Annie Jenkins',
'account balance' : 129.95,
}



#ACTIVITIES:
#1. Change name to Miss Bonnie
pet1['name'] = 'Miss Bonnie'

#2. Increase age by 1

pet1['age'] += 1

#3. Create another pet who is a dog, fill in all the fields

pet2 = {
    'name' : 'Jeremy',
    'animal category' : 'Dog',
    'age' : 19,
    'vaccinated' : False,
    'credit card' : '5678 1456 8245 2395',
    'billing address' : '13 Starkie Street, Leichhardt 2698',
    'owner name' : 'Benjamin',
    'account balance' : 0.35
}
def print_pet(pet):
    print(' ')
    for item in pet:
        print(item, ':', pet[item])
    print(' ')

print_pet(pet1)
print_pet(pet2)