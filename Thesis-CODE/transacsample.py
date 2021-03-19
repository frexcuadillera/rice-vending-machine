from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def exit_():
        win.destroy()
        import admin_items
def transac():
    
        global win
        win =Tk()
        load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
        render = ImageTk.PhotoImage(load)
        img = Label(win, image=render)
        img.image = render
        img.place(x=0, y=0)        
                

        wrapper1 = LabelFrame(win,bg="chartreuse3")

        topcolor = Label(win,text="Sales Report",bg="chartreuse3", fg="yellow", font="Sans-serif 30 bold",width=29, pady=10)
        topcolor.place(relx=0,rely=0)

        bottomcolor = Label(win,bg="chartreuse3", width=100, height=5)
        bottomcolor.place(relx=0,rely=0.82)

        label = Label(win,text="\tAmount \t\t   \tDate\t                Time\t\t",bg="gray",fg="yellow",font="Sans-serif 12 bold ")
        label.place(relx=0.06,rely=0.15)

        mycanvas = Canvas(wrapper1,width=550)
        mycanvas.pack(side=LEFT,fill="y",expand="yes")

        yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill="y")

        mycanvas.configure(yscrollcommand=yscrollbar.set)

        mycanvas.bind("<Configure>",lambda e:mycanvas.configure(scrollregion = mycanvas.bbox("all")))

        myframe= Frame(mycanvas)
        mycanvas.create_window((0,0),window=myframe,anchor="nw")

        wrapper1.pack(fill="both", expand="yes",pady="100",padx="50")

        file = open(r"/home/pi/Desktop/Thesis-CODE/transaction.txt")
        label1 = Label(myframe,text=file.read(),width=60, font="Sans-serif 12").pack()

        button = Button(win,text="Exit", width=5, pady=4,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=exit_)
        button.place(relx=0.43,rely=0.85)



        win.geometry("800x480")
        win.resizable(False,False)
        win.title("Transactions")
        win.attributes("-fullscreen",True)


#        win.mainloop()
transac()