from tkinter import *
from save_interrupt import *
from PIL import Image, ImageTk
import keysample


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
                import save_interrupt
                
                
                
            
            
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
        key = PhotoImage(file = r"/home/pi/Desktop/Thesis-CODE/keeyy.png")
        load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
        render = ImageTk.PhotoImage(load)
        img = Label(function, image=render)
        img.image = render
        img.place(x=0, y=0)

        Label (function,text="Automated Rice Vending Machine",bg="chartreuse3", fg="yellow", font="Sans-serif 30 bold", width=50, pady=10).pack()
        tb0= Entry (function, textvariable=l[0], font="sans-serif 40 bold", width=11,relief=GROOVE, justify=CENTER)
        tb0.place(relx=0.27,rely=0.2)
        keyboard1 = Button(function,image = key,width=35,height=35, bg="gray", fg="black",relief=GROOVE,command=lambda:keysample.create(function, tb0))
        keyboard1.place(relx=0.735,rely=0.258)
        label = Label(function, background="yellow", width="46", height=12,relief=GROOVE)
        label.place(relx=0.3, rely= 0.41)

        
       
        label0 = Label (function, background="chartreuse3", width="150", height=7)
        label0.place(relx=0, rely= 0.85)
        
        
        tbweight = Label (function,text="PRICE", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        tbweight.place(relx=0.31, rely=0.35)
        tb1 = Entry (function, textvariable=l[1], fg="black", font="sans-serif 12 bold", width=10)
        tb1.place(relx=0.35, rely=0.45)
        keyboard2 = Button(function,image = key,width=35,height=20, bg="gray", fg="black",relief=GROOVE,command=lambda:keysample.create(function, tb1))
        keyboard2.place(relx=0.5,rely=0.45)
        tb2 = Entry (function, textvariable=l[2], fg="black", font="sans-serif 12 bold", width=10)
        tb2.place(relx=0.35, rely=0.53)
        keyboard3 = Button(function,image = key,width=35,height=20, bg="gray", fg="black",relief=GROOVE,command=lambda:keysample.create(function, tb2))
        keyboard3.place(relx=0.5,rely=0.53)
        tb3 = Entry (function, textvariable=l[3], fg="black", font="sans-serif 12 bold", width=10)
        tb3.place(relx=0.35, rely=0.61)
        keyboard4 = Button(function,image = key,width=35,height=20, bg="gray", fg="black",relief=GROOVE,command=lambda:keysample.create(function, tb3))
        keyboard4.place(relx=0.5,rely=0.61)
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
        
        function.mainloop()
edit()
