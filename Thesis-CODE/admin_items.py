from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def admin():

        #def exit_edit():
#        gui.destroy()
#        import main_screen
#def transaction_list():
#    
#        gui.destroy()
#        import transacsample
##    def edits():
##        
##        import edit
            
#main function:
        
    global gui
    gui = Toplevel()
    gui.title("Microcontroller-Based Automated Rice Vending Machine")
    gui.geometry("800x480")
    gui.resizable(False,False)
    gui.attributes("-fullscreen",True)



    load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(gui, image=render)
    img.image = render
    img.place(x=0, y=0)
##        
    try:
        f = open("price.txt", "r")
    except:
        f = open("price.txt", "w")
        l = f.write("Angelica\n1kg\n1 1/2kg\n1 2kg")
        f = open("price.txt", "r")

    l = f.readlines()


    f.close()
        
    title1 = Label(gui,text="Microcontroller-Based Automated Rice Vending Machine",bg="chartreuse3", fg="yellow", font="Sans-serif 18 bold", width=50, pady=10)
    title1.place(relx=0,rely=0)
    tb0= Label(gui, text=l[0],bg= "chartreuse3",fg="yellow", font="sans-serif 40 bold", width=10,relief=GROOVE)
    tb0.place(relx=0.5,rely=0.2)
    label = Label(gui, background="yellow", width="46", height=11)
    label.place(relx=0.5, rely= 0.41)

    transaclabel = Label(gui, text="Transactions", bg="chartreuse3",relief=GROOVE, width=15,font="sans-serif 22 bold",padx=5)
    transaclabel.place(relx=0.040, rely=0.4)

#        lcontainer = Label(gui,text="DAILY REPORT",font="sans-serif 12 ",background="linen",  width=29, height=10,relief=RIDGE)
#        lcontainer.place(relx=0.045, rely=0.41)
       
    label0 = Label(gui, background="chartreuse3",relief=GROOVE, width="150", height=7)
    label0.place(relx=0, rely= 0.85)
        
        
    tbweight = Label(gui, text="Weight", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
    tbweight.place(relx=0.51, rely=0.35)
    tb1 = Label(gui, text=l[1], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb1.place(relx=0.55, rely=0.45)
    tb2 = Label(gui, text=l[2], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb2.place(relx=0.55, rely=0.53)
    tb3 = Label(gui, text=l[3], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb3.place(relx=0.55, rely=0.61)

        
    tbprice = Label(gui, text="Price", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
    tbprice.place(relx=0.72, rely=0.35)
    tb6 = Label(gui, text="P50.00", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb6.place(relx=0.78, rely=0.45)
    tb7 = Label(gui, text="P80.00", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb7.place(relx=0.78, rely=0.53)
    tb8 = Label(gui, text="P100.00", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb8.place(relx=0.78, rely=0.61)

    button0 = Button(gui, text="View", pady=2,width=20, bg="gray",relief=GROOVE, fg="yellow", font="sans-serif 15 bold ", command=transac)
    button0.place(relx=0.040, rely=0.5)
    button_1 = Button(gui, text="Edit", pady=4,width=7,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=edit)
    button_1.place(relx=0.4, rely=0.89)
    button_2 = Button(gui, text="Exit", width=5, pady=4,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=gui.destroy)
    button_2.place(relx=0.0, rely=0.89)
##
        
def edit():
        def edit_val(tbl_get, def_value):
                if tbl_get == None:
                        val = def_value
                else:
                        val = tbl_get

                return val

        def goback():
                f = open("price.txt", "w+")
                val0 = edit_val(tb0.get(), "Angelica")
                val1 = edit_val(tb1.get(), "P50.00")
                val2 = edit_val(tb2.get(), "P80.00")
                val3 = edit_val(tb3.get(), "P100.00")
                
                f.write("%s\n%s\n%s\n%s"%(val0,val1,val2,val3))
                f.close()
                function.destroy()
                save_interrupt()
                
                
                
            
            
#main function:
        global function
        function = Toplevel()
        function.title("Automated Rice Vending Machine")
        function.frame
        function.geometry("800x480")
        function.attributes("-fullscreen",True)

        function.resizable(False,False)
        

        
        try:
                f = open("price.txt", "r")
        except:
                f = open("price.txt", "w")
                l = f.write("Angelica\nP50.00\nP80.00\nP100.00")
                f = open("price.txt", "r")

        l = f.readlines()


        f.close()

        load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
        render = ImageTk.PhotoImage(load)
        img = Label(function, image=render)
        img.image = render
        img.place(x=0, y=0)

        Label (function,text="Automated Rice Vending Machine",bg="chartreuse3", fg="yellow", font="Sans-serif 30 bold", width=50, pady=10).pack()
        tb0= Entry (function, textvariable=l[0],fg="yellow", font="sans-serif 40 bold", width=11,relief=GROOVE, justify=CENTER)
        tb0.place(relx=0.27,rely=0.2)
        label = Label(function, background="yellow", width="46", height=12,relief=GROOVE)
        label.place(relx=0.3, rely= 0.41)

        
       
        label0 = Label (function, background="chartreuse3", width="150", height=7)
        label0.place(relx=0, rely= 0.85)
        
        
        tbweight = Label (function,text="PRICE", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        tbweight.place(relx=0.31, rely=0.35)
        tb1 = Entry (function, textvariable=l[1], fg="black", font="sans-serif 12 bold", width=10)
        tb1.place(relx=0.35, rely=0.45)
        tb2 = Entry (function, textvariable=l[2], fg="black", font="sans-serif 12 bold", width=10)
        tb2.place(relx=0.35, rely=0.53)
        tb3 = Entry (function, textvariable=l[3], fg="black", font="sans-serif 12 bold", width=10)
        tb3.place(relx=0.35, rely=0.61)
#        tb4 = Entry (gui, textvariable=l[4], fg="black", font="sans-serif 12 bold", width=10)
#        tb4.place(relx=0.35, rely=0.69)
#        tb5 = Entry (gui, textvariable=l[5], fg="black", font="sans-serif 12 bold", width=10)
#        tb5.place(relx=0.35, rely=0.77)

        
        tbprice = Label (function, text="WEIGHT", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        tbprice.place(relx=0.56, rely=0.35)
        tb6 = Label (function, text="1 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb6.place(relx=0.58, rely=0.45)
        tb7 = Label (function, text="1 1/2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb7.place(relx=0.58, rely=0.53)
        tb8 = Label (function, text="2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb8.place(relx=0.58, rely=0.61)
#        tb9 = Label (gui, text="P90.00", bg="yellow", fg="black", font="sans-serif 12 bold")
#        tb9.place(relx=0.58, rely=0.69)
#        tb10 = Label (gui, text="P100.00", bg="yellow", fg="black", font="sans-serif 12 bold")
#        tb10.place(relx=0.58, rely=0.77)

        button1 = Button(function, text="SAVE",  pady=4,width=7,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command = goback)
        button1.place(relx=0.61, rely=0.89)
        button2 = Button(function, text="Back",  pady=4,width=7,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command = function.destroy)
        button2.place(relx=0.3, rely=0.89)
        
#        function.mainloop()
#edit()

def exit_():
        win.destroy()
        import admin_items
def transac():
        gui.destroy()
        global win
        win =Toplevel()
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

        label = Label(win,text="\tAmount \t\t     Date\t \t             Time\t\t",bg="gray",fg="yellow",font="Sans-serif 12 bold ")
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
        label1 = Label(myframe,text=file.read(), font="Sans-serif 12").pack()

        button = Button(win,text="Exit", width=5, pady=4,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=exit_)
        button.place(relx=0.43,rely=0.85)



        win.geometry("800x480")
        win.resizable(False,False)
        win.title("Transactions")
        win.attributes("-fullscreen",True)

        
#        gui.mainloop()
#admin()
