from tkinter import *
import os

def register():
    
    global register_screen
    register_screen =Tk()
    register_screen.title("Register")
    register_screen.geometry("576x317")
    register_screen.frame
    register_screen.resizable(False,False)

    bg = Canvas(register_screen, height=39, width=0)
    filename = PhotoImage(file = "C:\\Users\\Jelmer\\Desktop\\Thesis-CODE\\2.png")
    background_label = Label(register_screen, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    labelreg = Label(register_screen, text="Please enter details below", bg="dodger blue", fg="blue4",  font="none 20 bold")
    labelreg.place(relx=0.2, rely=0.1)
    username_label = Label(register_screen, text="Username", bg="dodger blue", fg="blue4")
    username_label.place(relx=0.4, rely=0.3)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.place(relx=0.35, rely=0.4)
    password_label = Label(register_screen, text="Password", bg="dodger blue", fg="blue4")
    password_label.place(relx=0.4, rely=0.5)
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.place(relx=0.35, rely=0.6)
    buttonreg = Label(register_screen, text="Register", width=10, height=1, bg="gray", fg="blue4")
    buttonreg.place(relx=0.38, rely=0.8)
    button = Label(register_screen, text="Cancel", bg="gray",fg="blue4", width=10, height=1 )
    button.place(relx=0.38, rely=0.9)
    

