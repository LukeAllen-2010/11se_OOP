name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95
# ACTIVITIES:
#Theere are many ways to complete these tasks. How will you do them?
#1 Increase age by 1 year
age += 1
#2 Change the address to 17 Park Street
billing_address = '17 Park Street, The Shire 2695'
#3 No longer vaccinated (change state of vaccinated)
vaccinated = False
#4 Prompt user for updated credit card number and save new number
ccard = input('What is your credit card number? ')
#5 Change owner name to Alex Jones
owner_name = 'Alex Jones'
#6 Subtract $25 from account balance
account_balance -= 25

print(name, animal_category, age, vaccinated, ccard, billing_address, owner_name, account_balance)
print(account_balance)
