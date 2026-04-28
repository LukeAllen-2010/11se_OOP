number_list = []
number_sum = 0
number_count = int(input("How many numbers do you have? "))
for i in range(number_count):
    number_list.append(int(input(f"What is number {i + 1}? ")))
for num in number_list:
    number_sum += num
average = round(number_sum/number_count, 1)
print(f"There were {number_count} numbers inputted. They were: {number_list}. The average of these numbers is {average}.")