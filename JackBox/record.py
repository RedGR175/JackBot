import pyautogui
from pynput.mouse import Listener
import keyboard
import time

# Create a list to store the click positions and timestamps
click_positions = []


# Function to stop recording when "X" key is pressed
def stop_recording(e):
    if e.name == 'x':
        with open(f'close.txt', 'w') as f:
            for pos, timestamp in click_positions:
                f.write(f"{pos[0]},{pos[1]},{timestamp}\n")
        listener.stop()
        exit()

# Register the "X" key to stop recording
keyboard.on_press_key('x', stop_recording)

# Function to record mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        timestamp = time.time()  # Get the current time
        click_positions.append(((x, y), timestamp))

# Create a listener to record mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()
