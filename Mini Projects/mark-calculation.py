Max = 0
Num_Students = int(input("How many students in the class? " ))
MarksData = []
MarkSum = 0

for stud in range(Num_Students):
    MarksData.append(int(input(f"What is mark number {stud + 1}: "))) # Adds a mark for each student to the list 'MarksData'

for Mark in MarksData:
    if Mark > Max: 
        Max = Mark # When the largest Mark is found, it will set it to max
    MarkSum += Mark # When loop is broken, all marks will be added together
Average = MarkSum/Num_Students
print(f"Max: {Max}, Average: {Average}") # Display Max, Average