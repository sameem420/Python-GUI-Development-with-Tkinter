from tkinter import *
from tkinter import ttk

root = Tk()

check_btn = ttk.Checkbutton(root, text="SPAM?").pack()

spam = StringVar()
spam.set("SPAM!")

# check_btn.config(variable = spam, onvalue = 'SPAM Please!', offvalue = 'Boo SPAM!')
# print(spam.get())

breakfast = StringVar()
ttk.Radiobutton(root, text="Eggs", variable= breakfast, value="Eggs").pack()

ttk.Radiobutton(root, text="Milk", variable= breakfast, value="Milk").pack()

root.mainloop()