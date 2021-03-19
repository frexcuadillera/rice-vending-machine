#import bg photo

from tkinter import *
from PIL import ImageTK
import tkMessageBox
import tkFont

app = Tk()
app.title("Welcome")
image2 = Image.open('C:\\Users\\Jelmer\\Desktop\\Thesis-CODE\\bg.gif')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w,h))

app.mainloop()
