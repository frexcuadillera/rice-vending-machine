from tkinter import *
import threading
#from current_time import *
from PIL import Image, ImageTk
import time
import sys


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

print("Tare done! Add weight now...")
def sense():
    try:
        val = max(0, int(hx.get_weight(5)))
        kilo =(val/1000)
        weight = ("{:.0f}".format(kilo))
        print(weight)
        return weight
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
        return 0
    
    
refreshTime = 1000     

gui = Tk()
gui.title("Automated Rice Vending Machine")
gui.geometry("800x480")
gui.attributes("-fullscreen",True)
    
Wcontainer.config(gui,text=weight,background="linen",height=2,  width=36,relief=RIDGE)
Wcontainer.place(relx=0.045, rely=0.7)
    