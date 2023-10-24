from tkinter import *

root = Tk()

one = Label(root, text="One", bg="red", fg="blue")
one.pack()

two = Label(root, text="One", bg="black", fg="green")
two.pack(fill=X)

three = Label(root, text="One", bg="black", fg="green")
three.pack(fill=Y, side=LEFT)

root.mainloop()
