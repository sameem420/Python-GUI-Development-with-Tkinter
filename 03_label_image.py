from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text="Hello Tkinter!")
label.pack()

label.config(text="Howdy, Tkinter!")
label.config(text="Howdy, Tkinter, It\'s been a long way")
label.config(wraplength=100)
label.config(justify=CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('Cairo', 16, 'bold'))
label.config(text = 'Howdy, Tkinter!')

logo = PhotoImage(file="python_logo.png")
label.config(image = logo)
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')



root.mainloop()