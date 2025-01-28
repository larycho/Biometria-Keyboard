from pynput import keyboard
import time

last_key = -1
start = time.time()
end = time.time()

def on_press(key):
    global last_key, start
    if last_key == -1:
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            last_key = key.char
            start = time.time()
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

def on_release(key):
    global last_key, end, start
    print('{0} released'.format(
        key))
    last_key = -1
    end = time.time()
    print('time elapsed: {0} seconds'.format(end - start))

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

