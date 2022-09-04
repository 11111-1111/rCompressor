from importlib.resources import open_binary
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import FileDialog
from tkinter.filedialog import askopenfilename
import os
file_name = None
root = Tk()

root.title("rCompressor v1.0")
root.geometry('500x600')
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1) # row is up-down
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(2, weight=1)

# Set the initial theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

def change_theme():
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
        theme_button.configure(text="Light Mode!")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")
        theme_button.configure(text="Dark Mode!")

def file_get_name() -> str:
    global file_name
    if (file_name != None):
        file_name = "blank"
        return askopenfilename()
    else:
        return "No Selected File"

title = ttk.Label(root, text= "rCompressor", font=("Arial", 32))
separator = ttk.Separator(root, orient='horizontal')
theme_button = ttk.Button(root, text="Light Mode!", command=change_theme)
select_file_button = ttk.Button(root, text= "Select File", command= file_get_name)
selected_filename = ttk.Label(root, text = file_get_name, borderwidth= 3, relief= "solid", font=("Arial", 15))

title.grid(row = 0, column = 0, columnspan=6)
separator.grid(sticky="ew")
select_file_button.grid(row = 1, column = 3, pady=10)
selected_filename.grid(row = 1, column = 1, pady= 10)
theme_button.grid(row = 2, column=3)


root.mainloop()