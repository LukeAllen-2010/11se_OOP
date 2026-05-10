# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class Pet():
    def __init__(self, name, animal_category, age, vaccination_status, credit_card, billing_address):
        self.name = name
        self.category = animal_category
        self.age = age
        self.vaccinated = vaccination_status
        self.ccard = credit_card
        self.billing_address = billing_address
        self.owner_name = ''
        self.account_balance = 0

    def print_vaccination_status(self):
        print('Vaccination Status:', self.vaccinated)

pet1 = Pet('Bonnie', 'Cat', 3, True, '3423 2326 7543 1234', '17 Park Drive, The Shire 3695', 'Annie Jenkins', 129.95)

pet2 = Pet('Foxy', 'Dog', 19, False, '5678 1456 8245 2395', '13 Starkie Street, Leichhardt 2698', 'Benjamin', 0.35)


#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)