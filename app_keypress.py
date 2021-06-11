#!python
from pynput import keyboard
# import keyboard

'''
pip3 install pynput
pip3 install keyboard
'''

def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(key))

def on_release(key):
    print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        print("STOP LISTENER")
        return False
    if key == keyboard.Key.f7:
        print("START TEST")
        return True
    if key == keyboard.Key.f8:
        print("STOP TEST")
        return True

# Collect events until released
with keyboard.Listener( on_press=on_press, on_release=on_release ) as listener:
    listener.join()
