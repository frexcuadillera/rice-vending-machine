#import modules
 
from tkinter import *
import os
import sys
#from Customer import *
from admin_items import *
from PIL import Image, ImageTk
from keyboard import *
# Designing window for registration
 
def register():
    
    global register_screen
    register_screen = Toplevel()
    register_screen.title("Register")
    register_screen.geometry("800x480")
    register_screen.frame
    register_screen.attributes("-fullscreen",True)

    register_screen.resizable(False,False)
    #register_screen.configure(background="dodger blue")
    
#    background = Canvas(register_screen, height=39, width=500)
#    filename = PhotoImage(file = "C:\\Users\\Jelmer\\Desktop\\Thesis-CODE\\2.png")
#    background_label = Label(register_screen, image=filename)
#    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(register_screen, image=render)
    img.image = render
    img.place(x=0, y=0)
    label0 = Label (register_screen, background="chartreuse3", width="150", height=7)
    label0.place(relx=0, rely= 0.85)
    buttonkey=Button (register_screen, text="Keyboard", width=10, bg="gray", fg="black", font="Sans-serif 10 ",relief=GROOVE,command=lambda:create(self, username_entry))
    buttonkey.place(relx=0.5, rely=0.6)
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
 
    labelreg = Label(register_screen, text="Please enter details below", bg="chartreuse3", fg="yellow", width= 50, pady=10, font="Sans-serif 30 bold") .pack()
    username_label = Label(register_screen, text="Username",bg="chartreuse3",fg="black", font="Sans-serif 20 ", relief=RIDGE, pady=2,padx=5)
    username_label.place(relx=0.25, rely=0.3)
    username_entry = Entry(register_screen, textvariable=username,bg="linen",font="Sans-serif 15 ",relief=GROOVE)
    username_entry.place(relx=0.45, rely=0.31)
    password_label = Label(register_screen, text="Password",bg="chartreuse3", fg="black", font="Sans-serif 20 ",relief=RIDGE,pady=2,padx=5)
    password_label.place(relx=0.25, rely=0.5)
    password_entry = Entry(register_screen, textvariable=password,bg="linen", show='*',font="Sans-serif 15 ",relief=GROOVE)
    password_entry.place(relx=0.45, rely=0.51)
    buttonreg = Button(register_screen, text="Register", width=10, bg="gray", fg="black", font="Sans-serif 20 ",relief=GROOVE, command = register_user)
    buttonreg.place(relx=0.4, rely=0.87)
    button = Button(register_screen, text="Cancel", bg="gray",fg="black",font="Sans-serif 20",padx=2,relief=GROOVE, command =register_screen_delete )
    button.place(relx=0.01, rely=0.87)
    
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel()
    login_screen.title("Login")
    login_screen.attributes("-fullscreen",True)

    login_screen.geometry("800x480")
    
#    background = Canvas(login_screen, height=500, width=500)
#    filename = PhotoImage(file = "C:\\Users\\Jelmer\\Desktop\\Thesis-CODE\\2.png")
#   background_label = Label(login_screen, image=filename)
#    background_label.place(x=1, y=0, relwidth=1, relheight=1)
    load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(login_screen, image=render)
    img.image = render
    img.place(x=0, y=0)
    label0 = Label (login_screen, background="chartreuse3", width="150", height=7)
    label0.place(relx=0, rely= 0.85)
    buttonkey=Button (login_screen, text="Keyboard", width=10, bg="gray", fg="black", font="Sans-serif 10 ",relief=GROOVE)
    buttonkey.place(relx=0.5, rely=0.6)
    
    labellog=Label(login_screen, text="Please enter details below to login",  width= 50, pady=10,fg="yellow", bg= "chartreuse3", font="Sans-serif 30 bold").pack()
    login_screen.configure(background = "dodger blue")
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    labellog1 = Label(login_screen, text="Username ", bg="chartreuse3",fg="black", font="Sans-serif 20 ",pady=2,padx=5,relief=RIDGE)
    labellog1.place(relx=0.25, rely=0.3)
    username_login_entry = Entry(login_screen, textvariable=username_verify,bg="linen",font="Sans-serif 15 ",relief=GROOVE)
    username_login_entry.place(relx=0.45, rely=0.31)
    labellog2 = Label(login_screen, text="Password ",bg="chartreuse3",fg="black", font="Sans-serif 20 ",pady=2,padx=5,relief=RIDGE)
    labellog2.place(relx=0.25, rely=0.5)
    password_login_entry = Entry(login_screen, textvariable=password_verify,bg="linen", show='*',font="Sans-serif 15 ",relief=GROOVE)
    password_login_entry.place(relx=0.45, rely=0.51)
    button = Button(login_screen, text="Login", bg="gray",  font="Sans-serif 20",relief=GROOVE, command = login_verify)
    button.place(relx=0.43, rely=0.87)
    button = Button(login_screen, text="Cancel", bg="gray", font="Sans-serif 20",relief=GROOVE, command =main_screen_delete )
    button.place(relx=0.01, rely=0.87)
   
    
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    label1 = Label(register_screen, text="Registration Success", fg="green", font="Sans-serif 15")
    label1.place(relx=0.4, rely=0.65)


# Implementing event on login button 

def login_verify():
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_screen.destroy()
            import admin_items
            
            
        else:
            password_not_recognised()
 
    else:
        user_not_found()
       
        
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
def main_screen_delete():
    login_screen.destroy()
    import main_screen
def register_screen_delete():
    register_screen.destroy()
    import main_screen
def delete_login_success():    
              
    import admin_items
    
    
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()



#Keyboard
            
alphabets = [
    ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace'],
    ['Tab','q','w','e','r','t','y','u','i','o','p','[',']',"\\"],
    ['Caps Lock','a','s','d','f','g','h','j','k','l',';',"'",'Enter'],
    ['Shift','z','x','c','v','b','n','m',',','.','/','Shift'],
    ['Space']
]    

uppercase = False  # use uppercase chars. 

def select(entry, value):
    global uppercase

    if value == "Space":
        value = ' '
    elif value == 'Enter':
        value = '\n'
    elif value == 'Tab':
        value = '\t'

    if value == "Backspace":
        if isinstance(entry, Entry):
            entry.delete(len(entry.get())-1, 'end')
        #elif isinstance(entry, Text):
        else: # Text
            entry.delete('end - 2c', 'end')
    elif value in ('Caps Lock', 'Shift'):
        uppercase = not uppercase # change True to False, or False to True
    else:
        if uppercase:
            value = value.upper()
 #       entry.insert('end', value)



def create(self, entry):

    window = Toplevel(self)
    window.configure(background='#74e216')
    window.wm_attributes("-alpha", 1)

    for y, row in enumerate(alphabets):


        x = 0

        #for x, text in enumerate(row):
        for text in row:

            if text in ('Enter', 'Shift', 'Backspace', 'Caps Lock'):
                width = 7
                columnspan = 1
            elif text == 'Space':
                width = 80
                columnspan = 20
            else:                
                width = 5
                columnspan = 1

            Button(window, text=text, width=width, 
                      command=lambda value=text: select(entry, value),
                      padx=2, pady=2, bd=5, bg="black", fg="white"
                     ).grid(row=y, column=x, columnspan=columnspan)

            x += columnspan

