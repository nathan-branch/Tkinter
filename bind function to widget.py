from tkinter import *

root = Tk()

def printName():
    print("My Name is Bill")

button1 = Button(root, text="Print Name", command=printName)
button1.pack()

#   -2nd way
def printName2(event):
    print("My name is Todd")
button2 = Button(root, text="Print Name2")
button2.bind("<Button-1>", printName2) #function when left click
button2.pack()


root.mainloop()
