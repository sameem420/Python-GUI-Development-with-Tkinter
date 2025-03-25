from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text="Click Me!")
button.pack()

button.config(text= "Press Me!")
logo = PhotoImage(file="python_logo.png")

button.config(image=logo, compound=LEFT)

small_logo = logo.subsample(8,8)

button.config(image=small_logo)

def callback():
    print("Clicked!!!")

button.config(command=callback)

root.mainloop()