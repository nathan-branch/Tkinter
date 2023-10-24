from tkinter import *

root = Tk()

photo = PhotoImage(file="eur_cell2.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()
