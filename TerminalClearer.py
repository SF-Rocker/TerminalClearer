import tkinter as tk
import subprocess
import os

# Function to clear the history
def clear_history():
    try:
        # Ensure the TERM environment variable is set (some terminals need this)
        env = os.environ.copy()
        env['TERM'] = 'xterm-256color'

        # Command 1: Clear bash history file and clear history in memory
        subprocess.run(['bash', '-c', 'cat /dev/null > ~/.bash_history && history -cw'], check=True, env=env)
        # Command 2: Clear history in memory
        subprocess.run(['bash', '-c', 'history -c'], check=True, env=env)
        # Optional: Clear the terminal screen
        subprocess.run(['clear'], check=True, env=env)
        
        # Update the label to show success
        status_label.config(text="History cleared successfully!", fg="green")
    except subprocess.CalledProcessError:
        # If an error occurs, update the label to show failure
        status_label.config(text="Error clearing history.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Terminal History Cleaner")

# Set the window size
root.geometry("300x150")

# Add a label for status
status_label = tk.Label(root, text="Press 'Clear History' to clear the terminal history.", wraplength=250)
status_label.pack(pady=10)

# Add a button to clear history
clear_button = tk.Button(root, text="Clear History", command=clear_history, width=20)
clear_button.pack(pady=20)

# Start the main loop
root.mainloop()



