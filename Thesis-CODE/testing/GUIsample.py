#the GUI importer
from tkinter import *


#key down fuction o yung pinipindot
def click():
	print("Working . . .")
#main function:

window = Tk()
window.title("Automated Rice Vending Machine")
window.frame
window.geometry("485x380")


#para magkakulay yung buong window
window.configure(background="dodger blue", height="10")


#mga label , background at position


#creating label
Label (window, text="Automated Rice Vending Machine",bg="dodger blue", fg="black", font="none 20 bold") .grid(row=0, column=0)
label = Label (window, background="green", width="70", height="20") .grid(row=1, column=0, sticky=W) 
label1= Label (label, text="ANGELICA", bg="green", fg="yellow", font="sans-serif 45 bold", width="10").grid(row=1, column=0, sticky=N)
tb = Label (label, text="Weight", bg="green", fg="black", font="none 12 ")
tb.place(relx=0.2, rely=0.3)
tb1 = Label (window, text="1kg", bg="green", fg="black", font="none 12 ")
tb1.place(relx=0.2, rely=0.35)
tb2 = Label (window, text="1 1/4kg", bg="green", fg="black", font="none 12 ")
tb2.place(relx=0.2, rely=0.40)
tb3 = Label (window, text="1 1/2kg", bg="green", fg="black", font="none 12 ")
tb3.place(relx=0.2, rely=0.46)
tb4 = Label (window, text="1 3/4kg", bg="green", fg="black", font="none 12 ")
tb4.place(relx=0.2, rely=0.5)
tb5 = Label (window, text="2kg", bg="green", fg="black", font="none 12 ")
tb5.place(relx=0.2, rely=0.56)


#Label (text="Weight", bg="green", fg="black", font="none 12 ") .grid(row=4, column=0)
#Label (text="Weight", bg="green", fg="black", font="none 12 ",height="2", width="41") .grid(row=5, column=0)
#Label (window, text="Weight", bg="green", fg="black", font="none 12 ",height="2", width="41") .grid(row=6, column=0)

#to create text entry box
#textentry = Entry(window, width=20, bg="white")
#textentry.grid(row=2, column=0, sticky=W)

#add a submit button
button1 = Button(label, text="Order", width=7, bg="gray", fg="black", font="none 15 bold ", command=click)
button1.place(relx=0.4, rely=0.7)
#create a textbox
#output = Text(window, width=75, height=6, wrap=WORD, background="white")
#output.grid(row=6, column=0, columnspan=2, sticky=W)

#exit label
#Label (window, text="Click to Exit:", bg="black", fg="white" , font="none 12 bold") .grid(row=7, column=0, sticky=W)

#exit function
#def close_window():
#	window.destroy()
#	exit()
	
# exit button
#Button(window, text="Exit", width=14, command=close_window) .grid(row=8, column=0, sticky=W)

###to run the main loop
window.mainloop()     
