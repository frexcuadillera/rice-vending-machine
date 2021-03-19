from tkinter import *
from edit import *
from transacsample import *
from PIL import Image, ImageTk



gui = Tk()
gui.title("Microcontroller-Based Automated Rice Vending Machine")
gui.geometry("800x480")
gui.resizable(False,False)
gui.attributes("-fullscreen",True)
#def exit_edit():
#        gui.destroy()
#        import main_screen
#def transaction_list():
#    
#        gui.destroy()
#        import transacsample
def edits():
        
        import edit

##
##        transaction_list = Toplevel(gui)
##        transaction_list.title("Transactions")
##        transaction_list.geometry("150x100")
##        Label(transaction_list, text="Invalid Password ").pack()
##        Button(transaction_list, text="OK", command=transaction_list_destroy).pack()
##        
##def transaction_list_destroy():
##        transaction_list.destroy()
##        
def admin():        
            
#main function: 
        global gui
       



        load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
        render = ImageTk.PhotoImage(load)
        img = Label(gui, image=render)
        img.image = render
        img.place(x=0, y=0)
        
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
##        tb4 = Label (gui, text=l[4], bg="yellow", fg="black", font="sans-serif 12 bold")
##        tb4.place(relx=0.55, rely=0.69)
##        tb5 = Label (gui, text=l[5], bg="yellow", fg="black", font="sans-serif 12 bold")
##        tb5.place(relx=0.55, rely=0.77)

        
        tbprice = Label(gui, text="Price", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        tbprice.place(relx=0.72, rely=0.35)
        tb6 = Label(gui, text="P50.00", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb6.place(relx=0.78, rely=0.45)
        tb7 = Label(gui, text="P80.00", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb7.place(relx=0.78, rely=0.53)
        tb8 = Label(gui, text="P100.00", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb8.place(relx=0.78, rely=0.61)
##        tb9 = Label (gui, text="P90.00", bg="yellow", fg="black", font="sans-serif 12 bold")
##        tb9.place(relx=0.78, rely=0.69)
##        tb10 = Label (gui, text="P100.00", bg="yellow", fg="black", font="sans-serif 12 bold")
##        tb10.place(relx=0.78, rely=0.77)

#        button0 = Button(gui, text="View", pady=2,width=20, bg="gray",relief=GROOVE, fg="yellow", font="sans-serif 15 bold ", command=transaction_list)
#        button0.place(relx=0.040, rely=0.5)
        button1 = Button(gui, text="Edit", pady=4,width=7,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=edits)
        button1.place(relx=0.4, rely=0.89)
        button2 = Button(gui, text="Exit", width=5, pady=4,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=gui.destroy)
        button2.place(relx=0.0, rely=0.89)
##
        

        
#        gui.mainloop()
admin()
