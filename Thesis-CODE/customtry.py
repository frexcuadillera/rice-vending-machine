from tkinter import *
import threading
#import testing1
import RPi.GPIO as GPIO
#from current_time import *
#import ServoBillAcceptor
import serial
from PIL import Image, ImageTk
import sys

gui = Tk()
gui.title("Automated Rice Vending Machine")
gui.geometry("800x480")
gui.attributes("-fullscreen",True)

refreshTime = 100

def Customer():
    
    Wcontainer = Label(gui)
 #   weight = sense()
#    def servo():
#        import ServoBillAcceptor
#    def go():
#        
#        import choice
#        ser = serial.Serial('/dev/ttyUSB0',9600)
#        import current_time
               

           
#main function:
        #gui.configure(background="dodger blue", height="10")

        #para magkakulay yung buong window
##        gui.configure(background="dodger blue")
##        background = Canvas(gui, height=500, width=500)
##        filename = PhotoImage(file = "C:\\Users\\Jelmer\\Desktop\\Thesis-CODE\\2.png")
##        background_label = Label(gui, image=filename)
##        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(gui, image=render)
    img.image = render
    img.place(x=0, y=0)
##        photo = PhotoImage(file = r"C:\\Users\\Jelmer\\Desktop\\Thesis-CODE\\2.png")
    try:
        f = open("price.txt", "r")
    except:
        f = open("price.txt", "w")
        l = f.write("Angelica\nP50.00\nP80.00\nP100.00")
        f = open("price.txt", "r")

    l = f.readlines
    f.close()
    
#
       
    Label (gui,text="Microcontroller-Based Automated Rice Vending Machine",bg="chartreuse3", fg="yellow", font="Sans-serif 18 bold", width=50, pady=10).pack()
    tb0 = Label(gui, text=l[0],bg= "chartreuse3",fg="yellow", font="sans-serif 40 bold", width=10,relief=GROOVE)
    tb0.place(relx=0.5,rely=0.2)
    label = Label(gui, background="yellow", width="46", height=12,relief=GROOVE)
    label.place(relx=0.501, rely= 0.41)
       
    label0 = Label(gui, background="chartreuse3", width="150", height=4)
    label0.place(relx=0, rely= 0.85)
    transaclabel = Label(gui, text="You have inserted",bg="chartreuse3",fg= "yellow",font="sans-serif 25 bold",relief=GROOVE,padx=5)
    transaclabel.place(relx=0.025, rely=0.25)
#para sa display
#text=servo()
#    lcontainer = Label(gui,text="servo",background="linen", width=36, height=10,relief=RIDGE)
#    lcontainer.place(relx=0.045, rely=0.41)
    
    
    Ccontainer = Label(gui,background="linen",width=37,height=8,relief=RIDGE)
    Ccontainer.place(relx=0.055, rely=0.35)
    Pcontainer = Label(gui,text='P',background="linen", font="sans-serif 70 bold ")
    Pcontainer.place(relx=0.058, rely=0.38)
#    Mcontainer = Label(gui,text=pulses,background="linen", font="sans-serif 70 bold ")
#    Mcontainer.place(relx=0.15, rely=0.38)
#    
#    weight=StringVar(val)
    Bcontainer = Label(gui,background="linen",width=37,height=3,relief=RIDGE)
    Bcontainer.place(relx=0.055, rely=0.68)
    Econtainer = Label(gui,text="AVAILABLE WEIGHT:",background="linen",font="sans-serif 15 bold",fg="red")
    Econtainer.place(relx=0.057, rely=0.71)
#    Wcontainer = Label(gui,text=weight,background="linen",font="sans-serif 25")
#    Wcontainer.place(relx=0.35, rely=0.69)
#            
        
    tbweight = Label(gui, text="PRICE", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
    tbweight.place(relx=0.52, rely=0.35)
    tb1 = Label (gui, text=l[1], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb1.place(relx=0.57, rely=0.45)
    tb2 = Label (gui, text=l[2], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb2.place(relx=0.57, rely=0.53)
    tb3 = Label (gui, text=l[3], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb3.place(relx=0.57, rely=0.61)
#        tb4 = Label (gui, text=l[4], bg="yellow", fg="black", font="sans-serif 12 bold")
#        tb4.place(relx=0.55, rely=0.69)
#        tb5 = Label (gui, text=l[5], bg="yellow", fg="black", font="sans-serif 12 bold")
#        tb5.place(relx=0.55, rely=0.77)

        
    tbprice = Label (gui, text="WEIGHT", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
    tbprice.place(relx=0.72, rely=0.35)
    tb6 = Label (gui, text="1 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb6.place(relx=0.78, rely=0.45)
    tb7 = Label (gui, text="1 1/2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb7.place(relx=0.78, rely=0.53)
    tb8 = Label (gui, text="2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb8.place(relx=0.78, rely=0.61)
#        tb9 = Label (gui, text="P90.00", bg="yellow", fg="black", font="sans-serif 12 bold")
#        tb9.place(relx=0.78, rely=0.69)
#        tb10 = Label (gui, text="P100.00", bg="yellow", fg="black", font="sans-serif 12 bold")
#        tb10.place(relx=0.78, rely=0.77)
#add command=go
    button1 = Button(gui, text="Order", width=7, bg="gray", fg="black", font="sans-serif 20 bold", command=choice)
    button1.place(relx=0.4, rely=0.87)

#    def sensor():
##        import ServoBillAcceptor
#        import example
##        
##            
##
#    thread_function1 = threading.Thread(target=Customer)
#    thread_function2 = threading.Thread(target=sensor)
###    thread_function3 = threading.Thread(target=ServoBillAcceptor)
##
##    thread_function1.daemon = True
##    thread_function2.daemon = True
###    thread_function3.daemon = True
##    
#    thread_function1.start()
#    thread_function2.start()
###    thread_function3.start()
#    gui.mainloop()
#Customer()

def update():
    
    #weight = sense()

 #   Mcontainer = Label(gui,text=pulses,background="linen", font="sans-serif 70 bold ")
##    Mcontainer.place(relx=0.15, rely=0.38)
#    Wcontainer = Label(gui,text=weight,background="linen",font="sans-serif 30",width=2)
#    Wcontainer.place(relx=0.35, rely=0.685)
#    gui.mainloop()
    gui.after(refreshTime,update)
gui.after(refreshTime,update)
#    update.close
Customer()
