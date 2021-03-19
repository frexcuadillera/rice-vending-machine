from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



def exit():
        transac.destroy()
        import admin_items

def transaction():
        global transac
        root=Tk()
        transac = Toplevel()
        transac.title("Automated Rice Vending Machine")
        transac.frame
        transac.geometry("800x480")
        transac.attributes("-fullscreen",True)

        transac.resizable(False,False)
        
        load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
        render = ImageTk.PhotoImage(load)
        img = Label(transac, image=render)
        img.image = render
        img.place(x=0, y=0)        
        
        file = open(r"/home/pi/Desktop/Thesis-CODE/transaction.txt")
#        array=[]
        
#        for line in (file.readlines()[-10:]):
#            x = line.split("\n")
#            array.append(x)
            
#            print(x[0],'\t',x[1])
        label=Label(root)
        label.place(relx=0,rely=0)
        label0 = Label(transac,text="Sales Report",bg="chartreuse3", fg="yellow", font="Sans-serif 30 bold", width=50, pady=10) .pack()
        label1 = Label(transac,text="Amount                     Date                         Time",bg="gray", fg="yellow", font="Sans-serif 12 bold", width=41,padx=0,pady=0)
        label1.place(relx=0.2,rely=0.2)
        
#        label1 = Label(transac,text="Sales Report",bg="chartreuse3", fg="yellow", font="Sans-serif 30 bold", width=50, pady=10) .pack()
        
        label2 = Label(transac,bg="chartreuse3", width=100, height=5)
        label2.place(relx=0,rely=0.82)
        label3 = Label(transac, text=file.read(), padx=20,pady=20, font="Sans-serif 12 ")
        label3.place(relx=0.2,rely=0.25)
        
#        text = Text(transac)
#        scrollbar = Scrollbar(transac,command=text.yview)
#        text.config(yscrollcommand=scrollbar.set)
#        scrollbar.place(relx=0.2,rely=0.2)
#        text.insert(END,array)
        
        button = Button(transac,text="Exit", width=5, pady=4,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=exit)
        button.place(relx=0.45,rely=0.85)
        gui.mainloop()
transaction()
