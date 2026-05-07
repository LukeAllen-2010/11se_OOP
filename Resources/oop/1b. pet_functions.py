name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95
pet_alive = False

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age += 1
  age += 1

def verify_credit_card(card_num):
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False

def vaccinate():
  global account_balance
  global vaccinated
  if verify_credit_card(input('What is your credit card number? ')) and account_balance - 39 > 0:
    account_balance -= 39
    account_balance = round(account_balance, 2)
    vaccinated = True
  else:
    print('Ensure credit card number is correct and account balance is sufficient')


help()
increase_age()
print(age)

print(verify_credit_card('1234 4334 1001 0000'))

if verify_credit_card(ccard) == True:
  account_balance -= 39


if vaccinated != True:
  print('Your pet contracted a disease and died')



#ACTIVITIES:
#There are many ways to complete these. How will you go about the job?
#1. Verify this number 1234 4334 1001 0000
#2. Ask the user for a credit card number and let them know if it is valid
#3. If the credit card is valid then reduce balance by $39
#4. Write and test a function to vaccinate Bonnie 

if verify_credit_card('1234 4334 1001 0000'):
  print('1234 4334 1001 0000 is accepted')

# if verify_credit_card(input('What is your credit card number? ')) and account_balance - 39 > 0:
#   account_balance -= 39
#   vaccinated = True

vaccinate()
print('Account balance:', account_balance, 'Vaccinated:', vaccinated)