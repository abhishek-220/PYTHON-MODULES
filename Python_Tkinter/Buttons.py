from tkinter import *

root = Tk()
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')

lbl = Label(root, text = "Are you a Geek?")
lbl2 = Label(root, text = "Are you a Geek?")
lbl.grid()
lbl2.grid()

def clicked():
    lbl.configure(text = "I just got clicked")
    lbl2.configure(text = "Now I am clicked!")

btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)

btn1 = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)
btn1.grid(column=1, row=1)
 
# Execute Tkinter
root.mainloop()