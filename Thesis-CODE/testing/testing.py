from tkinter import *

def start():

        label = Label(master, text="First Name: %s\n" % (e1.get())).grid(row=0)
        label1 = Label(master, text="Last Name: %s" % (e2.get())).grid(row=1)
        e1.delete(0, label.END)
        e2.delete(0, label1.END)

master = Tk()
label = Label(master, text="First Name").grid(row=0)
label1 = Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

button = Button(master,text='Quit', command=master.quit).grid(row=3, column=0, sticky=W ,pady=4)
button1 = Button(master, text='Show', command=start).grid(row=3, column=1, sticky=W, pady=4)

master.mainloop()    
start()
