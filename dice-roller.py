import random
from tkinter import *

root=Tk()
root.geometry("700x450")

l1=Label(root,font=("roboto",200))

#the fn
def rolld():
    num=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(num)}{random.choice(num)}')
    l1.pack()

#button code+postion
b1=Button(root,text="Roll",command=rolld)
b1.place(x=320,y=10)

root.mainloop()
