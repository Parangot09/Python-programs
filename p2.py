from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("test program")
win.config(bg="#25383C")
in1 = Entry(win,font="monospace")
in1.place(x=50,y=60)
in2 = Entry(win,font="monospace")
in2.place(x=50,y=90)

def clf():
    rs = in1.get() + in2.get()
    box = Label(win,text= rs)
    box.place(x=50,y=200)

b1 = Button(win,text="combine",command= clf,font="monospace")
b1.place(x=50,y=150)








win.mainloop()
