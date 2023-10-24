from tkinter import *

root = Tk()

#   --TEXT PROMPTS
label1 = Label(root, text="Name")
label2 = Label(root, text="Password")

#   --input fields
entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
checkbox = Checkbutton(root, text="Keep Me Logged In")
checkbox.grid(columnspan=2)

root.mainloop()
