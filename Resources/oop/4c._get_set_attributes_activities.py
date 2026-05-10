class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    def set_weight(self, weight):
        if type(weight) == int or type(weight) == float:
            if weight > 0:
                self.weight = weight
            else:
                print(f'You inputted {weight}. Weight must be greater than zero')
        else:
            print(f'You inputted a {type(weight)}. Weight must be a number')

    def get_weight(self):
        return self.weight
   

#ACTIVITIES:
#1. Add attribute weight and write a getter method for weight
#2. Add setter method for weight and make sure it is a positive number (integer or float)