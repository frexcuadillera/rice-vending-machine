import tkinter as tk
from PIL import Image, ImageTk
import os
from subprocess import call
########## CONFIG ##########

# TKINTER FRAME
win = tk.Tk()
win.title('AUTOMATED RICE VENDING MACHINE')
win.resizable(False, False)
win.attributes('-fullscreen', True)
win.geometry("800x480")

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
 


# CONSTANTS
refreshTime = 1000 #in milliseconds

# COLOR CODES
green = '#00aa00'
yellow = '#ffff00'
black = '#111111'
white = '#ffffff'
gray = '#dddddd'

# ORDER SCREEN
order__topPanel = tk.Label(win)
order__insertLabel = tk.Label(win)
order__insertDisplay = tk.Label(win)
order__riceBrandLabel = tk.Label(win)
order__listHeader = tk.Label(win)
order__list = tk.Label(win)
order__bottomPanel =  tk.Label(win)
order__orderButton = tk.Button(win)

# ORDER SCREEN
def order():
    order__topPanel.place(relx = 0,
                          rely = 0,
                          relwidth = 1,
                          relheight = 0.15)
    order__topPanel.config(text = 'Automated Rice Vending Machine',
                           bg = green,
                           fg = yellow,
                           font = 20)
    order__insertLabel.place(relx = 0.2,
                             rely = 0.23,
                             relwidth = 0.28,
                             relheight = 0.1)
    order__insertLabel.config(text = 'You have inserted',
                              bg = green,
                              fg = black,
                              font = 20)
    order__insertDisplay.place(relx = 0.2,
                               rely = 0.33,
                               relwidth = 0.28,
                               relheight = 0.4)
    order__insertDisplay.config(text = 'P50.00',
                                bg = white,
                                fg = black,
                                font = 20)
    order__riceBrandLabel.place(relx = 0.52,
                                rely = 0.23,
                                relwidth = 0.28,
                                relheight = 0.1)
    order__riceBrandLabel.config(text = 'Angelica',
                                 bg = green,
                                 fg = yellow,
                                 font = 20)
    order__listHeader.place(relx = 0.52,
                            rely = 0.33,
                            relwidth = 0.28,
                            relheight = 0.08)
    order__listHeader.config(text = 'Price\t\tWeight',
                             bg = green,
                             fg = black,
                             font = 20,
                             justify = 'left')
    order__list.place(relx = 0.52,
                      rely = 0.41,
                      relwidth = 0.28,
                      relheight = 0.32)
    order__list.config(text = '''P50.00\t\t1 kg
                               \nP80.00\t\t1 1/2 kg
                               \nP100.00\t\t 2 kg''',
                       bg = yellow,
                       fg = black,
                       font = 20,
                       justify = 'left')
    order__bottomPanel.place(relx = 0,
                             rely = 0.85,
                             relwidth = 1,
                             relheight = 0.15)
    order__bottomPanel.config(bg = green)
    order__orderButton.place(relx = 0.4,
                             rely = 0.87,
                             relwidth = 0.2,
                             relheight = 0.11)
    order__orderButton.config(text = 'Order',
                              bg = gray,
                              fg = black,
                              font = 20)


def clear():
    order__topPanel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__insertLabel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__insertDisplay.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__riceBrandLabel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__listHeader.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__list.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__bottomPanel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__orderButton.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)


def update():
    clear()
    
    weight = sense()
    order__insertDisplay.config(text =weight,
                                bg = white,
                                fg = black,
                                font = 20)

    
    win.after(refreshTime, update)
win.after(refreshTime, update)
