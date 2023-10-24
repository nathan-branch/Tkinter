from tkinter import *
import sys


class PrintLogger():
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert(END, text);

    def flush(self):
        pass;

if __name__ == '__main__':
    def doSomething():
        print('I did something');
        root.after(1000, doSomething);
    
    root = Tk();
    t = Text();
    t.pack()

    pl = PrintLogger(t);

    sys.stdout = pl

    root.after(1000, doSomething)

    #mainloop
    root.mainloop()