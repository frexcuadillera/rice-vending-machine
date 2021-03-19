#from tkinter import *
#from ServoBillAcceptor import *
import serial
#import threading
#
#gui = Tk()
#gui.title("Automated Rice Vending Machine")
#gui.geometry("400x400")
#gui.attributes("-fullscreen",True)
#pulses = ser

ser = serial.Serial('/dev/ttyUSB0', 9600)
    
#pulses = ser.readline()
def money():
    pulses = 0

    while 1:        
        if(ser.in_waiting >0):
            pulses = ser.readline()
            pulses = int(pulses.decode('ascii'))
    #            pulses = int(pulses.decode('ascii').split('\n').split('\r'))
            print(pulses)
           
           
           
            credit = str(pulses)

##        return str(pulses)

                
            f = open("pulses.txt", "w+")
            f.write(credit)
            f.close()
            
#def main(gui):
#    pulses = money()
#    Label(gui, text = pulses).pack()
#    label3 = Label(gui, text="Thank You!",bg='limegreen',fg='white', font="Sans-serif 50 ")
#    label3.place(relx=0.25, rely= 0.25)
#    label4 = Label(gui, text="(CLICK OK TO FINISH)",bg="limegreen", fg="forestgreen",font="Sans-serif 15 bold")
#    label4.place(relx=0.33, rely= 0.42)
##            f = open("pulses.txt", "w+")
##            f.write(pulses)
##            f.close()
##
#    gui.mainloop()
#    
#
#
#thread_function1 = threading.Thread(target=money)
#thread_function2 = threading.Thread(target=main)
#thread_function1.start()
#thread_function2.start()
#
##print (1>=0)

