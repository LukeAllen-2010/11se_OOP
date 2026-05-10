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
        self.vaccinate = True

    def clear_balance(self):
        self.account_balance = 0
    
    def print_age(self):
        if self.category == 'Dog':
            print('Age in human years is', self.age * 7)
        elif self.catergory == 'Cat':
            print('Age in human years is', self.age * 6)

p1 = Pet('Bonnie', 'Cat', 9, 149.50)

p1.clear_balance
p1.have_birthday
p1.vaccinate
p1.print_age

print(p1.account_balance, p1.vaccinated, p1.age)
    
    

#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have completed each activity correctly.