from tkinter import *
from admin_items import *


def y():
    save.destroy()
    admin_items()
    
    

def save():
        global save
        save = Tk()
        save.title("Transaction")
        save.geometry("150x100")
        Label(save, text="Do you want to Proceed?").pack()
        button1 = Button(save, text="Yes", command=y).pack()
        button2 = Button(save, text="NO", command=save.destroy).pack()

#        save.mainloop()
#ave()