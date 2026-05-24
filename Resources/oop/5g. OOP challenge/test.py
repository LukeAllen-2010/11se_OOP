import time

def print_line(message, delay = 0.1):
    for character in message:
        print(character, end='', flush=True)
        time.sleep(delay)

print_line('hi jason', delay = 0.12)
# import time
# message = 'stupid'
# for i in message:
#     print(i, end='', flush=True)  # Print numbers as soon as they are generated
#     # print(i, end=" ", flush=False)  # Print everything together at the end
#     time.sleep(0.5)

# print("end")