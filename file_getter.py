import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    os.system('''osascript -e 'tell application "System Events" to set frontmost of process "Python" to true' ''')
    file_path = filedialog.askdirectory()  # Open file dialog
    if file_path:
        return file_path

def pop():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    dir = open_file()  # Call the function to open the file dialog
    return dir
    root.mainloop()

print(pop()) 