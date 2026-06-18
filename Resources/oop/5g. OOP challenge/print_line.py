import time

def print_line(message, delay = 0.1):
    PAUSE = {'.' : 2, '?' : 3, '!' : 3, ',' : 1.5, ' ' : 0.25}
    for character in message:
        print(character, end='', flush=True)
        if character in PAUSE:
            time.sleep(delay*PAUSE[character])
        else:
            time.sleep(delay)
