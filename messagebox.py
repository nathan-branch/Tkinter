from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('window title', 'Monkeys can live up to 300 years')

answer = tkinter.messagebox.askquestion('Question 1', 'do you like me')

if answer == 'yes':
    print('*==*')

root.mainloop()
