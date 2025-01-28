from pynput import keyboard
import time
import numpy as np
import string
import statistics

last_key = -1 # Stores last key pressed

start = time.time() # Key press timestamps: start of press, end of press
end = time.time()

start_find = time.time() # Key release timestamps: start of release, end of release
end_find = time.time()

# Initialization of arrays that are going to store data
key_hold_times = np.zeros(26) # Time it takes to hold down a key
key_find_times = np.zeros(26) # Time it takes to find a key

key_hold_avg_times = []
key_find_avg_times = []

for i in range(26):
    key_hold_avg_times.append([])
    key_find_avg_times.append([])


def on_press(key):
    global last_key, start, end_find, start_dinf

    if last_key == -1: # If no other key is being held down
        try:
            print('alphanumeric key {0} pressed'.format(key.char))

            last_key = key.char

            start = time.time()
            end_find = time.time()

            # Converts letter to its position in the latin alphabet (1 - a, 2 - b, etc.)
            index = string.ascii_lowercase.index(key.char)
            if 0 <= index <= 25:
                # Adding values to arrays that track the time elapsed between key presses
                key_find_times[index] = end_find - start_find
                key_find_avg_times[index].append(end_find - start_find)

        except (AttributeError, ValueError): # Throws error when special key (esc, shift, etc.) or number pressed
            print('special key {0} pressed'.format(key))

def on_release(key):
    global last_key, end, start, start_find

    print('{0} released'.format(key))

    last_key = -1
    end = time.time()
    start_find = time.time()

    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
    try:
        # Converts letter to its position in the latin alphabet (1 - a, 2 - b, etc.)
        index = string.ascii_lowercase.index(key.char) 
        if 0 <= index <= 25:
            # Adding values to arrays that track time when pressing down keys
            key_hold_times[index] = end - start
            key_hold_avg_times[index].append(end - start)

    except (AttributeError, ValueError): # Throws if special key or number pressed
        print('special key {0} pressed'.format(key))



# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


# Calculating averages
for i in range(26):

    if key_hold_avg_times[i]: # If a key was pressed, calculate average hold time
        key_hold_avg_times[i] = statistics.mean(key_hold_avg_times[i])
    else: # If the key wasn't pressed, default to 0.
        key_hold_avg_times[i] = 0.

    if key_find_avg_times[i]:
        key_find_avg_times[i] = statistics.mean(key_find_avg_times[i])
    else:
        key_find_avg_times[i] = 0.



print(key_hold_times)
print(key_find_times)

print(key_hold_avg_times)
print(key_find_avg_times)