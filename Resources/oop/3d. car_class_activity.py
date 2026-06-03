# Learning intentions:
# - Create a car class example
# - Use attributes: make, model, year and price
# - Create a __str__ method that prints make and model

class Car:
    def __init__(self,make,model,year,price, for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = for_sale

    def __str__(self):
        return f'Make: {self.make}, Model: {self.model}, For Sale = {self.for_sale}'

c1 = Car('Mazda', '6', 2005)
c2 = Car('Toyota', '4', 2001)
c3 = Car('Hyundai', '3', 1999)
c4 = Car('Mazda', '3', '2000')

cars = [c1, c2, c3, c4]

for car in cars:
    print(car)


#ACTIVITIES:
#1. Istantiate another car object ✅
#2. Add another attribute (for_sale) ✅
#3. Add sale status for sale or not for sale to the __str__ method ✅
#4. Create 2 more cars and print all car statuses with a loop ✅