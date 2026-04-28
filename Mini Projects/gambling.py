from random import *
iteration = 0
pool = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
lucky = []
for i in range(6):
    rand_num = randint(1, 45-i) # Uses random to generate a random number out of the amount of numbers in the list
    chosen_num = pool[rand_num] # Uses rand_num to generate the random lotto number
    pool.remove(chosen_num)
    lucky.append(chosen_num)
print(lucky)