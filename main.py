from pynput import keyboard
import time
import numpy as np
import string

last_key = -1
start = time.time()
end = time.time()
key_hold_times = np.zeros(26)

def on_press(key):
    global last_key, start

    if last_key == -1: # If no other key is being held down
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
            last_key = key.char
            start = time.time()
        except AttributeError: # Throws error when special key pressed (esc, shift, etc.)
            print('special key {0} pressed'.format(key))

def on_release(key):
    global last_key, end, start

    print('{0} released'.format(key))
    last_key = -1
    end = time.time()

    print('time elapsed: {0} seconds'.format(end - start))

    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
    try:
        index = string.ascii_lowercase.index(key.char) # Converts letter to its position in the latin alphabet (1 - a, 2 - b, etc.)
        if 0 <= index <= 25:
            key_hold_times[index] = end - start

    except (AttributeError, ValueError): # Throws if special key or number pressed
        print('special key {0} pressed'.format(key))

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print(key_hold_times)