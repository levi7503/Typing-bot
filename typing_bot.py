import time
import pyautogui

time.sleep(5)  # Sleep for 5 seconds to allow time to switch to the target window

# Safely opening the file and reading its contents
with open("text.txt", "r") as text:
    for each_line in text:
        pyautogui.typewrite(each_line)
        time.sleep(10)  # Typewrite the contents of the file

# The file is automatically closed when exiting the 'with' block.
