from tkinter import *
import threading
import ServoBillAcceptor




gui = Tk()
gui.title("Automated Rice Vending Machine")
gui.geometry("400x400")
#gui.attributes("-fullscreen",True


billThread = threading.Thread(target = ServoBillAcceptor.bill()
)
#guithread= threading.Thread(target = func)
#
billThread.start()
#guithread.start()

gui()



#print (1>=0)