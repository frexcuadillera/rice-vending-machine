#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
import keysample
from PIL import Image, ImageTk
import os
from subprocess import call
def main_account_screen():
    def shutdown():
        call("sudo poweroff",shell=True)
    def start():
        main_screen.destroy()
        import Customer
        
    global main_screen
    main_screen = Tk()
    main_screen.title("Welcome Page")
    main_screen.frame
    main_screen.attributes("-fullscreen",True)
    main_screen.geometry("800x480")
    main_screen.resizable(False,False)

#para magkakulay yung buong window
##    main_screen.configure(background="dodger blue")
##    background = Canvas(main_screen, height=500, width=500)
##    filename = PhotoImage(file = "C:\\Users\\Jelmer\\Desktop\\Thesis-CODE\\2.png")
##    background_label = Label(main_screen, image=filename)
##    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(main_screen, image=render)
    img.image = render
    img.place(x=0, y=0)
    photo = PhotoImage(file = r"/home/pi/Desktop/Thesis-CODE/button1.png")
    photo1 = PhotoImage(file = r"/home/pi/Desktop/Thesis-CODE/buttonsamplead.png")
    photo2= PhotoImage(file = r"/home/pi/Desktop/Thesis-CODE/Newowner.png")
    photo3= PhotoImage(file = r"/home/pi/Desktop/Thesis-CODE/Start.png")    
#label
    label=Label (main_screen,text="Microcontroller-Based Automated Rice Vending Machine",bg="chartreuse3", fg="yellow", font="Sans-serif 18 bold", width=50, pady=10).pack()
    label0 = Label (main_screen,background="chartreuse3",width="150", height=7)
    label0.place(relx=0, rely= 0.85)
    button_admin = Button(main_screen,image=photo1,width=250,height=60, command=login)
    button_admin.place(relx=0.35, rely=0.2)
    button_new_admin = Button(main_screen,image=photo2,width=250,height=60, command=register)
    button_new_admin.place(relx=0.35, rely=0.4)
    button_start = Button(main_screen,image=photo3,width=250,height=60, command=start)
    button_start.place(relx=0.35, rely=0.6)
    button_shutdown = Button(main_screen,image = photo,width=60, height=65,bg="black", command=shutdown)
    button_shutdown.place(relx=0.0, rely=0.85)

#    def sensor():
#        import example
            
#def sensor1():
#    
#    
#    
#    
#    thread_function1 = threading.Thread(target=main_account_screen)
#    thread_function2 = threading.Thread(target=sensor)
#
#    thread_function1.start()
#    thread_function2.start()
    #   
#    
    
#)


    main_screen.mainloop()
    
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
    
    
    keyboard1 = Button(register_screen, text="Keyboard", width=8, bg="gray", fg="black", font="Sans-serif 12 ",relief=GROOVE,command=lambda:keysample.create(register_screen,username_entry ))
    keyboard1.place(relx=0.8, rely=0.31)
    keyboard2 = Button(register_screen, text="Keyboard", width=8, bg="gray", fg="black", font="Sans-serif 12 ",relief=GROOVE,command=lambda:keysample.create(register_screen, password_entry))
    keyboard2.place(relx=0.8, rely=0.51)



    
    buttonreg = Button(register_screen, text="Register", width=10, bg="gray", fg="black", font="Sans-serif 20 ",relief=GROOVE, command = register_user)
    buttonreg.place(relx=0.43, rely=0.87)
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

    key = PhotoImage(file = r"/home/pi/Desktop/Thesis-CODE/keeyy.png")
        
    load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(login_screen, image=render)
    img.image = render
    img.place(x=0, y=0)
    label0 = Label (login_screen, background="chartreuse3", width="150", height=7)
    label0.place(relx=0, rely= 0.85)
    
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
    
    keyboard1 = Button(login_screen, text="Keyboard", width=8, bg="gray", fg="black", font="Sans-serif 12 ",relief=GROOVE,command=lambda:keysample.create(login_screen, username_login_entry))
    keyboard1.place(relx=0.8, rely=0.31)
    keyboard2 = Button(login_screen, text="Keyboard", width=8, bg="gray", fg="black", font="Sans-serif 12 ",relief=GROOVE,command=lambda:keysample.create(login_screen, password_login_entry))
    keyboard2.place(relx=0.8, rely=0.51)
    
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
            admin()
            
            
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
    
def register_screen_delete():
    register_screen.destroy()
    
def delete_login_success():    
              
    admin()
    
    
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()







            

def admin():

        #def exit_edit():
#        gui.destroy()
#        import main_screen
#def transaction_list():
#    
#        gui.destroy()
#        import transacsample
##    def edits():
##        
##        import edit
            
#main function:
        
    global gui
    gui = Toplevel()
    gui.title("Microcontroller-Based Automated Rice Vending Machine")
    gui.geometry("800x480")
    gui.resizable(False,False)
    gui.attributes("-fullscreen",True)



    load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(gui, image=render)
    img.image = render
    img.place(x=0, y=0)
##        
    try:
        f = open("price.txt", "r")
    except:
        f = open("price.txt", "w")
        l = f.write("Angelica\nP50.00\nP80.00\nP100.00")
        f = open("price.txt", "r")

    l = f.readlines()


    f.close()
        
    title1 = Label(gui,text="Microcontroller-Based Automated Rice Vending Machine",bg="chartreuse3", fg="yellow", font="Sans-serif 18 bold", width=50, pady=10)
    title1.place(relx=0,rely=0)
    tb0= Label(gui, text=l[0],bg= "chartreuse3",fg="yellow", font="sans-serif 40 bold", width=10,relief=GROOVE)
    tb0.place(relx=0.5,rely=0.2)
    label = Label(gui, background="yellow", width="46", height=11)
    label.place(relx=0.5, rely= 0.41)

    transaclabel = Label(gui, text="Transactions", bg="chartreuse3",relief=GROOVE, width=15,font="sans-serif 22 bold",padx=5)
    transaclabel.place(relx=0.040, rely=0.4)

#        lcontainer = Label(gui,text="DAILY REPORT",font="sans-serif 12 ",background="linen",  width=29, height=10,relief=RIDGE)
#        lcontainer.place(relx=0.045, rely=0.41)
       
    label0 = Label(gui, background="chartreuse3",relief=GROOVE, width="150", height=7)
    label0.place(relx=0, rely= 0.85)
        
        
    tbweight = Label(gui, text="Weight", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
    tbweight.place(relx=0.51, rely=0.35)
    tb1 = Label(gui, text='1 KG', bg="yellow", fg="black", font="sans-serif 12 bold")
    tb1.place(relx=0.55, rely=0.45)
    tb2 = Label(gui, text="1 1/2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb2.place(relx=0.55, rely=0.53)
    tb3 = Label(gui, text="2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
    tb3.place(relx=0.55, rely=0.61)

        
    tbprice = Label(gui, text="Price", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
    tbprice.place(relx=0.72, rely=0.35)
    tb6 = Label(gui, text=l[1], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb6.place(relx=0.78, rely=0.45)
    tb7 = Label(gui, text=l[2], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb7.place(relx=0.78, rely=0.53)
    tb8 = Label(gui, text=l[3], bg="yellow", fg="black", font="sans-serif 12 bold")
    tb8.place(relx=0.78, rely=0.61)

    button0 = Button(gui, text="View", pady=2,width=20, bg="gray",relief=GROOVE, fg="yellow", font="sans-serif 15 bold ", command=transac)
    button0.place(relx=0.040, rely=0.5)
    button_1 = Button(gui, text="Edit", pady=4,width=7,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=edit)
    button_1.place(relx=0.4, rely=0.89)
    button_2 = Button(gui, text="Exit", width=5, pady=4,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=gui.destroy)
    button_2.place(relx=0.0, rely=0.89)
##
        
def edit():
        def edit_val(tbl_get, def_value):
                if tbl_get == None:
                        val = def_value
                else:
                        val = tbl_get

                return val

        def goback():
                f = open("price.txt", "w+")
                val0 = edit_val(tb0.get(), "Angelica")
                val1 = edit_val(tb1.get(), "P50.00")
                val2 = edit_val(tb2.get(), "P80.00")
                val3 = edit_val(tb3.get(), "P100.00")
                
                f.write("%s\n%s\n%s\n%s"%(val0,val1,val2,val3))
                f.close()
                function.destroy()
                import save_interrupt
                
                
                
            
            
#main function:
        gui.destroy()
        global function
        function = Toplevel()
        function.title("Automated Rice Vending Machine")
        function.frame
        function.geometry("800x480")
        function.attributes("-fullscreen",True)

        function.resizable(False,False)
        

        
        try:
                f = open("price.txt", "r")
        except:
                f = open("price.txt", "w")
                l = f.write("Angelica\nP50.00\nP80.00\nP100.00")
                f = open("price.txt", "r")

        l = f.readlines()


        f.close()

        key = PhotoImage(file = r"/home/pi/Desktop/Thesis-CODE/keeyy.png")
        load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
        render = ImageTk.PhotoImage(load)
        img = Label(function, image=render)
        img.image = render
        img.place(x=0, y=0)

        Label (function,text="Automated Rice Vending Machine",bg="chartreuse3", fg="yellow", font="Sans-serif 30 bold", width=50, pady=10).pack()
        tb0= Entry (function, textvariable=l[0], font="sans-serif 40 bold", width=11,relief=GROOVE, justify=CENTER)
        tb0.place(relx=0.27,rely=0.2)
        keyboard1 = Button(function,image = key,width=35,height=35, bg="gray", fg="black",relief=GROOVE,command=lambda:keysample.create(function, tb0))
        keyboard1.place(relx=0.735,rely=0.258)
        label = Label(function, background="yellow", width="46", height=12,relief=GROOVE)
        label.place(relx=0.3, rely= 0.41)

        
       
        label0 = Label (function, background="chartreuse3", width="150", height=7)
        label0.place(relx=0, rely= 0.85)
        
        
        tbweight = Label (function,text="PRICE", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        tbweight.place(relx=0.31, rely=0.35)
        tb1 = Entry (function, textvariable=l[1], fg="black", font="sans-serif 12 bold", width=10)
        tb1.place(relx=0.35, rely=0.45)
        keyboard2 = Button(function,image = key,width=35,height=20, bg="gray", fg="black",relief=GROOVE,command=lambda:keysample.create(function, tb1))
        keyboard2.place(relx=0.5,rely=0.45)
        tb2 = Entry (function, textvariable=l[2], fg="black", font="sans-serif 12 bold", width=10)
        tb2.place(relx=0.35, rely=0.53)
        keyboard3 = Button(function,image = key,width=35,height=20, bg="gray", fg="black",relief=GROOVE,command=lambda:keysample.create(function, tb2))
        keyboard3.place(relx=0.5,rely=0.53)
        tb3 = Entry (function, textvariable=l[3], fg="black", font="sans-serif 12 bold", width=10)
        tb3.place(relx=0.35, rely=0.61)
        keyboard4 = Button(function,image = key,width=35,height=20, bg="gray", fg="black",relief=GROOVE,command=lambda:keysample.create(function, tb3))
        keyboard4.place(relx=0.5,rely=0.61)
#        tb4 = Entry (gui, textvariable=l[4], fg="black", font="sans-serif 12 bold", width=10)
#        tb4.place(relx=0.35, rely=0.69)
#        tb5 = Entry (gui, textvariable=l[5], fg="black", font="sans-serif 12 bold", width=10)
#        tb5.place(relx=0.35, rely=0.77)

        
        tbprice = Label (function, text="WEIGHT", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        tbprice.place(relx=0.56, rely=0.35)
        tb6 = Label (function, text="1 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb6.place(relx=0.58, rely=0.45)
        tb7 = Label (function, text="1 1/2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb7.place(relx=0.58, rely=0.53)
        tb8 = Label (function, text="2 KG", bg="yellow", fg="black", font="sans-serif 12 bold")
        tb8.place(relx=0.58, rely=0.61)
#        tb9 = Label (gui, text="P90.00", bg="yellow", fg="black", font="sans-serif 12 bold")
#        tb9.place(relx=0.58, rely=0.69)
#        tb10 = Label (gui, text="P100.00", bg="yellow", fg="black", font="sans-serif 12 bold")
#        tb10.place(relx=0.58, rely=0.77)

        button1 = Button(function, text="SAVE",  pady=4,width=7,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command = goback)
        button1.place(relx=0.61, rely=0.89)
        button2 = Button(function, text="Back",  pady=4,width=7,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command = function.destroy)
        button2.place(relx=0.3, rely=0.89)
        
        function.mainloop()
#edit()

def exit_():
        win.destroy()
        admin()
def transac():
        gui.destroy()
        global win
        win =Toplevel()
        load = Image.open("/home/pi/Desktop/Thesis-CODE/2.png")
        render = ImageTk.PhotoImage(load)
        img = Label(win, image=render)
        img.image = render
        img.place(x=0, y=0)        
                

        wrapper1 = LabelFrame(win,bg="chartreuse3")

        topcolor = Label(win,text="Sales Report",bg="chartreuse3", fg="yellow", font="Sans-serif 30 bold",width=29, pady=10)
        topcolor.place(relx=0,rely=0)

        bottomcolor = Label(win,bg="chartreuse3", width=100, height=5)
        bottomcolor.place(relx=0,rely=0.82)

        label = Label(win,text="\tAmount \t\t   Date\t\t\tTime  \t    \t",bg="gray",fg="yellow",font="Sans-serif 12 bold ")
        label.place(relx=0.06,rely=0.15)

        mycanvas = Canvas(wrapper1,width=550)
        mycanvas.pack(side=LEFT,fill="y",expand="yes")

        yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill="y")

        mycanvas.configure(yscrollcommand=yscrollbar.set)

        mycanvas.bind("<Configure>",lambda e:mycanvas.configure(scrollregion = mycanvas.bbox("all")))

        myframe= Frame(mycanvas)
        mycanvas.create_window((0,0),window=myframe,anchor="nw")

        wrapper1.pack(fill="both", expand="yes",pady="100",padx="50")

        file = open(r"/home/pi/Desktop/Thesis-CODE/transaction.txt")
        label1 = Label(myframe,text=file.read(),width=50, font="Sans-serif 12").pack()

        button = Button(win,text="Exit", width=5, pady=4,relief=GROOVE, bg="gray", fg="black", font="sans-serif 15 bold ", command=exit_)
        button.place(relx=0.43,rely=0.85)



        win.geometry("800x480")
        win.resizable(False,False)
        win.title("Transactions")
        win.attributes("-fullscreen",True)

        
#        gui.mainloop()
#admin()


    
    
   
 
main_account_screen()

