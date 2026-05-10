# Learning intentions:
# - Create a method (function belonging to a class)
# - Discuss the use of attributes in the method

class Pet:
    def __init__(self, name, category, age, account_balance):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = account_balance
    
    def have_birthday(self):
        self.age += 1
    
    def vaccinate(self):
        self.vaccinate
    
    

#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have comeplted each activity correctly.