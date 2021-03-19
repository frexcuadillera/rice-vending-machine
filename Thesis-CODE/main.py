from tkinter import *
import time
import threading
import RPi.GPIO as GPIO
#from current_time import *
#import ServoBillAcceptor
from PIL import Image, ImageTk
import sys
import serial
import os

gui = Tk()
gui.title("Automated Rice Vending Machine")
gui.geometry("800x480")
gui.attributes("-fullscreen",True)

credit = 0
weight = 0

device0 = '/dev/ttyUSB0'
device1 = '/dev/ttyUSB1'

def billAcceptor():
    serialbuffer = 0
    ser = None
    
    try:
        ser = serial.Serial(device0, 9600)
    except:
        try:
            ser = serial.Serial(device1, 9600)
        except Exception as ex:
            print(ex)
            
    while True:
        serialbuffer = ser.readline().decode("utf-8").lstrip().rstrip()
        global credit
        credit += int(serialbuffer)
        #print(credit)
  
EMULATE_HX711=False

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711
hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(-113)
hx.reset()

hx.tare()

#print("Tare done! Add weight now...")

def sense():
    try:
        val = max(0, int(hx.get_weight(5)))
        kilo =(val/1000)
        weight = ("{:.0f}".format(kilo))
        #print(weight)
 
        f = open("weight.txt", "w+")
        f.write(weight)
        f.close()
        return weight
 
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
        return 0
    
def ok():
    choice_screen.destroy()
    global credit
    credit = 0

def order():
    
    gui.quit()
    global choice_screen
    choice_screen = Tk()
    choice_screen.title("Transaction")
    choice_screen.geometry("800x480")
    choice_screen.attributes("-fullscreen",True)

    label0 = Label (choice_screen, background="limegreen", width="100", height=80)
    label0.place(relx=0, rely= 0)

    label3 = Label(choice_screen, text="Thank You!",bg='limegreen',fg='white', font="Sans-serif 50 ")
    label3.place(relx=0.25, rely= 0.25)
    label4 = Label(choice_screen, text="(CLICK OK TO FINISH)",bg="limegreen", fg="forestgreen",font="Sans-serif 15 bold")
    label4.place(relx=0.33, rely= 0.42)
    button1 = Button(choice_screen, text="OK",fg='white',bg='darkgreen',width=18,height=2,font="Sans-serif 20 bold", command=ok)
    button1.place(relx=0.26, rely= 0.7)
    
img = ""

#pag uupdate ng pera at weight

def update():
    Mcontainer.configure(text=credit)
    Wcontainer.configure(text=weight)
    gui.after(100, update)
    

def Customer():

    load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(gui, image=render)
    img.image = render
    img.place(x=0, y=0)
       
    try:
        f = open("price.txt", "r")
    except:
        f = open("price.txt", "w")
        l = f.write("Angelica\nP50.00\nP80.00\nP100.00")
        f = open("price.txt", "r")

    l = f.readlines()

    f.close()
       
    Label (gui,text="Microcontroller-Based Automated Rice Vending Machine",bg="chartreuse3", fg="yellow", font="Sans-serif 18 bold", width=50, pady=10).pack()
    tb0 = Label(gui, text=l[0],bg= "chartreuse3",fg="yellow", font="sans-serif 40 bold", width=10,relief=GROOVE)
    tb0.place(relx=0.5,rely=0.2)
    label = Label(gui, background="yellow", width="46", height=12,relief=GROOVE)
    label.place(relx=0.501, rely= 0.41)
       
    label0 = Label(gui, background="chartreuse3", width="150", height=4)
    label0.place(relx=0, rely= 0.85)
    transaclabel = Label(gui, text="You have inserted",bg="chartreuse3",fg= "yellow",font="sans-serif 25 bold",relief=GROOVE,padx=5)
    transaclabel.place(relx=0.025, rely=0.25)

    Ccontainer = Label(gui,background="linen",width=37,height=8,relief=RIDGE)
    Ccontainer.place(relx=0.055, rely=0.35)
    Pcontainer = Label(gui,text='P',background="linen", font="sans-serif 70 bold ")
    Pcontainer.place(relx=0.058, rely=0.38)

    Bcontainer = Label(gui,background="linen",width=37,height=3,relief=RIDGE)
    Bcontainer.place(relx=0.055, rely=0.68)
    Econtainer = Label(gui,text="AVAILABLE WEIGHT:",background="linen",font="sans-serif 15 bold",fg="red")
    Econtainer.place(relx=0.057, rely=0.71)

        
    tbweight = Label(gui, text="PRICE", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
    tbweight.place(relx=0.52, rely=0.35)
    tb1 = Label (gui, text=l[1], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb1.place(relx=0.57, rely=0.45)
    tb2 = Label (gui, text=l[2], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb2.place(relx=0.57, rely=0.53)
    tb3 = Label (gui, text=l[3], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb3.place(relx=0.57, rely=0.61)
   
    tbprice = Label (gui, text="WEIGHT", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
    tbprice.place(relx=0.72, rely=0.35)
    tb6 = Label (gui, text="1 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb6.place(relx=0.78, rely=0.45)
    tb7 = Label (gui, text="1 1/2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb7.place(relx=0.78, rely=0.53)
    tb8 = Label (gui, text="2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb8.place(relx=0.78, rely=0.61)

    button1 = Button(gui, text="Order", width=7, bg="gray", fg="black", font="sans-serif 20 bold", command=order)
    button1.place(relx=0.4, rely=0.87)
    global Mcontainer
    global Wcontainer
    Mcontainer = Label(gui,text=credit,background="linen", font="sans-serif 70 bold ")
    Mcontainer.place(relx=0.15, rely=0.38)
    Wcontainer = Label(gui,text=weight,background="linen",font="sans-serif 30",width=2)
    Wcontainer.place(relx=0.35, rely=0.685)
    update()
    gui.mainloop()
    
    
threading.Thread(target=billAcceptor).start()
Customer()




