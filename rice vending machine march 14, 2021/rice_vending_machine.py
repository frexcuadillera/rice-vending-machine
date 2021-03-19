from tkinter import *
from PIL import ImageTk, Image
import sys
from tkinter import messagebox
import tkinter as tk
import threading
import RPi.GPIO as GPIO
import time
import serial
import sqlite3
import datetime
#import math



hf = '#74e216'  #header and footer
dl = '#306700'  #dark line
bgm = '#c0ea9d' #middle

#database
#con = sqlite3.connect('rice_vending_machine.db')
#cursor = con.cursor()

class VendingMachine(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomePage, AdminLogin, AdminPage, AdminChangeAccount,
                  AdminChangePrice, SeeTransactions, StartPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row =0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class WelcomePage(tk.Frame):
 
    def __init__(self, master, controller):
        Frame.__init__(self,master)


        #header
        TopFrame = tk.Frame(self, bg=hf)
        TopFrame.grid(column=0, row=0, padx=(0, 0), sticky="nsew")
        TopFrame.grid_rowconfigure(0, weight=1)
        TopFrame.grid_columnconfigure(0, weight=1)

        #header label
        self.label1 = tk.Label(TopFrame, text="Rice Vending Machine",
                               font =("Arial, 18"),
                               bg = hf,
                               width = 60,
                               height = 2)
        self.label1.grid(column=0, row=0)

        #Darkgreen line Top
        TopFrameB = tk.Frame(self, height = 10)
        TopFrameB.grid(column = 0, row =1)

        #Middle Buttons
                                     
        ButtonsFrame = tk.Frame(self)
        ButtonsFrame.grid(column = 0, row =2, sticky ="ew")
        ButtonsFrame.configure(background = '#c0ea9d')
        
        
        self.width = 25
        self.height = 2
        self.padx = (270,0)
        self.pady = 18

        #Button 1
        self.button1 = HoverButton(ButtonsFrame,
                                   bg = hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0,
                                   command=lambda: controller.show_frame(StartPage))
        self.img = ImageTk.PhotoImage(Image.open("start2.png"))
        self.button1.config(image=self.img, width = 310, height = 70)
        self.button1.grid(column = 0, row = 0,
                          padx = self.padx, pady = self.pady)
        
        #Button 2
#        self.button2 = HoverButton(ButtonsFrame,
#                                   bg =hf,
#                                   activebackground=dl,
#                                   relief= "flat",
#                                   highlightthickness=0,
#                                   command=lambda: controller.show_frame(SeePrice))
#        self.img1 = ImageTk.PhotoImage(Image.open("price2.png"))
#        self.button2.config(image=self.img1, width = 310, height = 70)
#        self.button2.grid(column = 0, row = 15,
#                          padx = self.padx, pady = self.pady)
        

        #Button 3
        self.button3 = HoverButton(ButtonsFrame,
                                   bg =hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0,
                                   command=lambda: controller.show_frame(AdminLogin))
        self.img2 = ImageTk.PhotoImage(Image.open("admin2.png"))
        self.button3.config(image=self.img2, width = 310, height = 70)
        self.button3.grid(column = 0, row = 30,
                          padx = self.padx, pady = self.pady)

        #Dark Green line Bottom
        BottomFrame1 = tk.Frame(self, height= 10)
        BottomFrame1.grid(column=0, row=3)

        #Footer
        BottomFrame = tk.Frame(self, height=70, bg=hf)
        BottomFrame.grid(column=0, row=4, sticky ="ew")

class AdminLogin(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        self.controller = controller


        #header
        TopFrame = Frame(self, bg=hf)
        TopFrame.grid(column=0, row=0, padx=(0, 0), sticky="nsew")
        TopFrame.grid_rowconfigure(0, weight=1)
        TopFrame.grid_columnconfigure(0, weight=1)
        
        #header label
        self.label1 = Label(TopFrame, text="Administrator",font =("Arial, 18"),bg = hf,width = 60,height = 2)
        self.label1.grid(column=0, row=0, sticky = "nsew")
        
        #back button
        self.firstbutton = HoverButton(TopFrame,bg = hf,
                                       activebackground=hf,
                                       relief= "flat",
                                       highlightthickness=0,
                                       command=lambda: controller.show_frame(WelcomePage))
        self.backbutton= ImageTk.PhotoImage(Image.open("back2.png"))
        self.firstbutton.config(image = self.backbutton, width=100, height=50)
        self.firstbutton.grid(column = 0, row = 0, sticky="w")

        #Darkgreen line Top
        TopFrameB = Frame(self, height = 10)
        TopFrameB.grid(column = 0, row =1)

        #Middle InfoFrame
        InfoFrame = Frame(self, bg=bgm)
        InfoFrame.grid(column = 0, row =2, sticky ="ew")

        #Middle Frame
                                     
        MidFrame = Frame(InfoFrame)
        MidFrame.grid(column = 0, row =0, sticky ="n", pady=(20,0), padx=(95,0))
        MidFrame.configure(background = bgm )
        
        
        self.width = 25
        self.height = 2
        self.padx = (120,0)
        self.pady = 20

        #login

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_login_entry
        global password_login_entry

        global answer_login

        self.userlabel = Label(MidFrame, text="Username: * ", bg=bgm, font =("Arial, 14"))
        self.userlabel.grid(column=1, row=0, padx = self.padx , pady = 40)
        username_login_entry = Entry(MidFrame, textvariable=username_verify, font =("Arial, 12"))
        username_login_entry.grid(column =2, row =0,padx = (20,0), pady= 40)
        firstkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, username_login_entry))
        firstkey_button.grid(column =3, row=0)
        
        self.passlabel = Label(MidFrame, text="Password: * ", bg = bgm,font=("Arial, 14"))
        self.passlabel.grid(column = 1, row = 3, padx = self.padx ,pady = self.pady)
        password_login_entry = Entry(MidFrame, textvariable=password_verify,  show= '*',font =("Arial, 12"))
        password_login_entry.grid(column = 2, row = 3, padx= (20,0), pady = self.pady)
        secondkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, password_login_entry))
        secondkey_button.grid(column =3, row=3)

        self.loginbutton = HoverButton(MidFrame, bg=hf, activebackground= dl, relief="flat", highlightthickness=0, command = self.login_verify)
        self.loginimg = ImageTk.PhotoImage(Image.open("login2.png"))
        self.loginbutton.config(image=self.loginimg, width = 80, height = 40)
        self.loginbutton.grid(column = 2, row = 4, pady=35)

        answer_login = Label(MidFrame, text = '', bg = bgm, fg = "red")
        answer_login.grid(column=2, row=5)
        
        
        #Dark Green line Bottom
        BottomFrame1 = Frame(self, height= 10)
        BottomFrame1.grid(column=0, row=3)

        #Footer
        BottomFrame = Frame(self, height=70, bg=hf)
        BottomFrame.grid(column=0, row=4, sticky ="ew")

        


    def login_verify(self):
        con = sqlite3.connect('rice_vending_machine.db')
        cursor = con.cursor()
        sql = "SELECT * FROM admin"
        cursor.execute(sql)
        con.commit()
        
        
        rows = cursor.fetchall()
        name = rows[0][0]
        password = rows[0][1]

        if username_verify.get() == name:
            if password_verify.get() == password:
                username_login_entry.delete(0, END)
                password_login_entry.delete(0, END)
                self.controller.show_frame(AdminPage)
                answer_login.config(text='')
            else:
                answer_login.config(text="Invalid Password")
                password_login_entry.delete(0, END)
        else:
            answer_login.config(text="User Not found")
            username_login_entry.delete(0, END)
            password_login_entry.delete(0, END)



class AdminPage(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)

        #header
        TopFrame = tk.Frame(self, bg=hf)
        TopFrame.grid(column=0, row=0, padx=(0, 0), sticky="nsew")
        TopFrame.grid_rowconfigure(0, weight=1)
        TopFrame.grid_columnconfigure(0, weight=1)

        #header label
        self.label1 = tk.Label(TopFrame, text="Administrator",
                               font =("Arial, 18"),
                               bg = hf,
                               width = 60,
                               height = 2)
        self.label1.grid(column=0, row=0, sticky = "nsew")
        
        self.firstbutton = HoverButton(TopFrame,
                                   bg = hf,
                                   activebackground=hf,
                                   relief= "flat",
                                   highlightthickness=0,
                                   command=lambda: controller.show_frame(WelcomePage))
        
        self.backbutton= ImageTk.PhotoImage(Image.open("back2.png"))
        self.firstbutton.config(image = self.backbutton, width=100, height=50)
        self.firstbutton.grid(column = 0, row = 0, sticky="w")
        
        


        #Darkgreen line Top
        TopFrameB = tk.Frame(self, height = 10)
        TopFrameB.grid(column = 0, row =1)

        #Middle Buttons
                                     
        ButtonsFrame = tk.Frame(self)
        ButtonsFrame.grid(column = 0, row =2, sticky ="ew")
        ButtonsFrame.configure(background = '#c0ea9d')
        
        
        self.width = 25
        self.height = 2
        self.padx = (270,0)
        self.pady = 18

        #Button 1
        self.button1 = HoverButton(ButtonsFrame,
                                   bg = hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0,
                                   command=lambda: controller.show_frame(AdminChangeAccount))
        self.img = ImageTk.PhotoImage(Image.open("changeaccount.png"))
        self.button1.config(image=self.img, width = 310, height = 70)
        self.button1.grid(column = 0, row = 0,
                          padx = self.padx, pady = self.pady)
        
        def adminChangePriceButton():
            controller.show_frame(AdminChangePrice)
            global riceText
            global onekgText
            global halfkgText
            global twokgText
            
            con = sqlite3.connect('rice_vending_machine.db')
            cursor = con.cursor()
            sql = "SELECT * FROM prices"
            cursor.execute(sql)
            con.commit()
            
            
            rows = cursor.fetchall()
            
            riceText.set(rows[0][0])
            onekgText.set(rows[0][1])
            halfkgText.set(rows[0][2])
            twokgText.set(rows[0][3])
            
        #Button 2
        self.button2 = HoverButton(ButtonsFrame,
                                   bg =hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0,
                                   command=lambda: adminChangePriceButton())
        self.img1 = ImageTk.PhotoImage(Image.open("changeprices.png"))
        self.button2.config(image=self.img1, width = 310, height = 70)
        self.button2.grid(column = 0, row = 15,
                          padx = self.padx, pady = self.pady)  
        
        #Button 3
        self.button3 = HoverButton(ButtonsFrame,
                                   bg =hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0,
                                   command=lambda: controller.show_frame(SeeTransactions))
        self.img2 = ImageTk.PhotoImage(Image.open("seetransactions2.png"))
        self.button3.config(image=self.img2, width = 310, height = 70)
        self.button3.grid(column = 0, row = 30,
                          padx = self.padx, pady = self.pady)

        #Dark Green line Bottom
        BottomFrame1 = tk.Frame(self, height= 10)
        BottomFrame1.grid(column=0, row=3)

        #Footer
        BottomFrame = tk.Frame(self, height=70, bg=hf)
        BottomFrame.grid(column=0, row=4, sticky ="ew")

        #Shutdown Button
        self.button4 = HoverButton(BottomFrame,
                                   bg =hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0)
        self.img3 = ImageTk.PhotoImage(Image.open("shut.png"))
        self.button4.config(image=self.img3, width = 60, height= 56)
        self.button4.grid(column = 0, row = 2,padx=(0, 0), pady=(10,0))

class AdminChangeAccount(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        self.controller = controller

        #header
        TopFrame = Frame(self, bg=hf)
        TopFrame.grid(column=0, row=0, padx=(0, 0), sticky="nsew")
        TopFrame.grid_rowconfigure(0, weight=1)
        TopFrame.grid_columnconfigure(0, weight=1)
        
        #header label
        self.label1 = Label(TopFrame, text="!!Change Account!!",font =("Arial, 18"),bg = hf,fg ="#FF0000",width = 60,height = 2)
        self.label1.grid(column=0, row=0, sticky = "nsew")
        
        self.firstbutton = HoverButton(TopFrame,bg = hf,
                                       activebackground=hf,relief= "flat",
                                       highlightthickness=0,
                                       command=lambda: controller.show_frame(AdminPage))
        self.backbutton= ImageTk.PhotoImage(Image.open("back2.png"))
        self.firstbutton.config(image = self.backbutton, width=100, height=50)
        self.firstbutton.grid(column = 0, row = 0, sticky="w")

        #Darkgreen line Top
        TopFrameB = Frame(self, height = 10)
        TopFrameB.grid(column = 0, row =1)

        #Middle InfoFrame
        InfoFrame = Frame(self, bg=bgm)
        InfoFrame.grid(column = 0, row =2, sticky ="ew")

        #Middle Frame
                            
        MidFrame = Frame(InfoFrame)
        MidFrame.grid(column = 0, row =0, sticky ="n", pady=(0,0), padx=(95,0))
        MidFrame.configure(background = bgm )
        
        
        
        self.width = 25
        self.height = 2
        self.padx = (50,0)
        self.pady = 13

        #login

        global username
        global password
        global username_entry
        global password_entry
        global confirm_password
        
        username = StringVar()
        password = StringVar()
        confirm_password = StringVar()
        
        global username_login_entry
        global password_login_entry
        global confirm_password_entry
        
        global answer
        
        self.username = Label(MidFrame, text="Username: * ", bg=bgm, font =("Arial, 14"))
        self.username.grid(column=1, row=0, padx = self.padx , pady = 40)
        username_entry = Entry(MidFrame, textvariable=username, font =("Arial, 12"))
        username_entry.grid(column =2, row =0,padx = (20,0))
        thirdkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, username_entry))
        thirdkey_button.grid(column =3, row=0)
        
        self.password = Label(MidFrame, text="Password: * ", bg = bgm,font=("Arial, 14"))
        self.password.grid(column = 1, row = 3, padx = self.padx ,pady = self.pady)
        password_entry = Entry(MidFrame, textvariable=password,  show= '*',font =("Arial, 12"))
        password_entry.grid(column = 2, row = 3, padx= (20,0), pady = self.pady)
        fourthkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, password_entry))
        fourthkey_button.grid(column =3, row=3)
        

        self.confirm_password = Label(MidFrame, text="Confirm Password: * ", bg = bgm, font=("Arial, 14"))
        self.confirm_password.grid(column = 1, row = 4, padx = self.padx ,pady = self.pady)
        confirm_password_entry = Entry(MidFrame, textvariable=confirm_password,  show= '*',font =("Arial, 12"))
        confirm_password_entry.grid(column = 2, row = 4, padx= (20,0), pady = self.pady)
        fifthkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, confirm_password_entry))
        fifthkey_button.grid(column =3, row=4)

        answer = Label(MidFrame, text = '', bg = bgm, fg = "red")
        answer.grid(column=2, row=5)
        

        self.loginbutton = HoverButton(MidFrame, bg=hf, activebackground= dl, relief="flat", highlightthickness=0,
                                        command = self.change_user)
        self.loginimg = ImageTk.PhotoImage(Image.open("submit.png"))
        self.loginbutton.config(image=self.loginimg, width = 80, height = 40)
        self.loginbutton.grid(column = 2, row = 6, pady=25)
        
        
        #Dark Green line Bottom
        BottomFrame1 = Frame(self, height= 10)
        BottomFrame1.grid(column=0, row=3)

        #Footer
        BottomFrame = Frame(self, height=70, bg=hf)
        BottomFrame.grid(column=0, row=4, sticky ="ew")

        


    def change_user(self):

        if len(username.get()) == 0 or len(password.get()) == 0 or len(confirm_password.get()) == 0:
            answer.config(text="Fields must be filled in")
        else:
            if password.get() != confirm_password.get():
                answer.config(text="Passwords Don't Match")
                password_entry.delete(0, END)
                confirm_password_entry.delete(0, END)
            else:
                #Delete previous record
                con = sqlite3.connect('rice_vending_machine.db')
                cursor = con.cursor()
                sql = "DELETE FROM admin"
                cursor.execute(sql)
                con.commit()
                
                
                #Insert new record
                con = sqlite3.connect('rice_vending_machine.db')
                cursor = con.cursor()
                sql = "INSERT INTO admin (username, password) VALUES (?,?)"
                cursor.execute(sql, (username.get(), password.get()))
                con.commit()
                

                username_entry.delete(0, END)
                password_entry.delete(0, END)
                confirm_password_entry.delete(0, END)
                self.controller.show_frame(AdminLogin)
                messagebox.showinfo("SUCCESSFUL", "Try to log in again")
                answer.config(text="")

class AdminChangePrice(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        self.controller = controller

        #header
        TopFrame = Frame(self, bg=hf)
        TopFrame.grid(column=0, row=0, padx=(0, 0), sticky="nsew")
        TopFrame.grid_rowconfigure(0, weight=1)
        TopFrame.grid_columnconfigure(0, weight=1)
        
        #header label
        self.label1 = Label(TopFrame, text="Change Prices",font =("Arial, 18"),bg = hf,fg ="#FF0000",width = 60,height = 2)
        self.label1.grid(column=0, row=0, sticky = "nsew")
        
        self.firstbutton = HoverButton(TopFrame,bg = hf,
                                       activebackground=hf,relief= "flat",
                                       highlightthickness=0,
                                       command=lambda: controller.show_frame(AdminPage))
        self.backbutton= ImageTk.PhotoImage(Image.open("back2.png"))
        self.firstbutton.config(image = self.backbutton, width=100, height=50)
        self.firstbutton.grid(column = 0, row = 0, sticky="w")

        #Darkgreen line Top
        TopFrameB = Frame(self, height = 10)
        TopFrameB.grid(column = 0, row =1)

        #Middle InfoFrame
        InfoFrame = Frame(self, bg=bgm)
        InfoFrame.grid(column = 0, row =2, sticky ="ew")

        #Middle Frame
                            
        MidFrame = Frame(InfoFrame)
        MidFrame.grid(column = 0, row =0, sticky ="n", pady=(0,0), padx=(95,0))
        MidFrame.configure(background = bgm )
        
        
        
        self.width = 25
        self.height = 2
        self.padx = (100,0)
        self.pady = 4
        
        global riceText
        global onekgText
        global halfkgText
        global twokgText

        riceText = StringVar()
        onekgText = StringVar()
        halfkgText = StringVar()
        twokgText = StringVar()

        global rice_entry
        global onekg_entry
        global halfkg_entry
        global twokg_entry
        
        con = sqlite3.connect('rice_vending_machine.db')
        cursor = con.cursor()
        sql = "SELECT * FROM prices"
        cursor.execute(sql)
        con.commit()
        
        
        rows = cursor.fetchall()

        global answer_price

        #placeholder_text = '0'

        self.rice = Label(MidFrame, text="Kind of Rice: * ", bg=bgm, font =("Arial, 14"))
        self.rice.grid(column=1, row=0, padx = self.padx , pady = 40)
        rice_entry = Entry(MidFrame, textvariable=riceText, font =("Arial, 12"))
        rice_entry.grid(column = 2, row =0, padx = (20,0))
        sixthkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, rice_entry))
        sixthkey_button.grid(column =3, row=0)
        
        self.onekg = Label(MidFrame, text="1 Kg: * ", bg = bgm, font=("Arial, 14"))
        self.onekg.grid(column = 1, row = 2, padx = self.padx ,pady = self.pady)
        onekg_entry = Entry(MidFrame, textvariable=onekgText,font =("Arial, 12"))
        onekg_entry.grid(column = 2, row = 2, padx= (20,0), pady = self.pady)
        #onekg_entry.insert(0, placeholder_text)
        seventhkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, onekg_entry))
        seventhkey_button.grid(column =3, row=2)

        
        self.halfkg = Label(MidFrame, text="1 1/2 Kg: * ", bg = bgm, font=("Arial, 14"))
        self.halfkg.grid(column = 1, row = 3, padx = self.padx ,pady = self.pady)
        halfkg_entry = Entry(MidFrame, textvariable=halfkgText,font =("Arial, 12"))
        halfkg_entry.grid(column = 2, row = 3, padx= (20,0), pady = self.pady)
        #halfkg_entry.insert(0, placeholder_text)
        eightkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, halfkg_entry))
        eightkey_button.grid(column =3, row=3)
        

        self.twokg = Label(MidFrame, text="2 Kg: * ", bg = bgm, font=("Arial, 14"))
        self.twokg.grid(column = 1, row = 4, padx = self.padx ,pady = self.pady)
        twokg_entry = Entry(MidFrame, textvariable=twokgText,font =("Arial, 12"))
        twokg_entry.grid(column = 2, row = 4, padx= (20,0), pady = self.pady)
        #twokg_entry.insert(0, placeholder_text)
        
        ninthkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, twokg_entry))
        ninthkey_button.grid(column =3, row=4)
        

        answer_price = Label(MidFrame, text="", bg = bgm, fg = "red")
        answer_price.grid(column = 2, row = 5)

        
        riceText.set(rows[0][0])
        onekgText.set(rows[0][1])
        halfkgText.set(rows[0][2])
        twokgText.set(rows[0][3])
        
        self.loginbutton = HoverButton(MidFrame, bg=hf, activebackground= dl, relief="flat", highlightthickness=0,
                                        command = self.change_price)
        self.loginimg = ImageTk.PhotoImage(Image.open("submit.png"))
        self.loginbutton.config(image=self.loginimg, width = 80, height = 40)
        self.loginbutton.grid(column = 2, row = 6, pady=25)

        
        
        
        #Dark Green line Bottom
        BottomFrame1 = Frame(self, height= 10)
        BottomFrame1.grid(column=0, row=3)

        #Footer
        BottomFrame = Frame(self, height=70, bg=hf)
        BottomFrame.grid(column=0, row=4, sticky ="ew")

        

    def change_price(self):
#        global rice
#        global onekg
#        global halfkg
#        global twokg
        
        global startPageRice
        global startPagePriceOne
        global startPagePriceHalf
        global startPagePriceTwo
        #if len(rice.get()) == 0 or len(onekg.get())==1 or len(halfkg.get())==1 or len(twokg.get())==1:
        if(False):
            answer_price.config(text="Fields must be filled in")
        else:
            try:
                #int(onekg.get())
                #int(halfkg.get())
                #int(twokg.get())
#                rice = StringVar()
#                onekg = StringVar()
#                halfkg = StringVar()
#                twokg = StringVar()
                
                #Delete previous record
                con = sqlite3.connect('rice_vending_machine.db')
                cursor = con.cursor()
                sql = "DELETE FROM prices"
                cursor.execute(sql)
                con.commit()
                
                
                #Insert new record
                con = sqlite3.connect('rice_vending_machine.db')
                cursor = con.cursor()
                sql = "INSERT INTO prices (rice, priceone, pricehalf, pricetwo) VALUES (?,?,?,?)"
                cursor.execute(sql, (rice_entry.get(), onekg_entry.get(), halfkg_entry.get(), twokg_entry.get()))
                con.commit()
                
                
                startPageRice = rice_entry.get()
                startPagePriceOne = onekg_entry.get()
                startPagePriceHalf = halfkg_entry.get()
                startPagePriceTwo = twokg_entry.get()

                rice_entry.delete(0, END)
                onekg_entry.delete(0, END)
                halfkg_entry.delete(0, END)
                twokg_entry.delete(0, END)
                answer_price.config(text="")
                self.controller.show_frame(AdminPage)
                messagebox.showinfo("SUCCESSFUL", "Successfully changed!")
                


                #THIS IS FOR THE DISPLAY OF DATA IN SEE PRICE PAGE
                con = sqlite3.connect('rice_vending_machine.db')
                cursor = con.cursor()
                sql = "SELECT * FROM prices"
                cursor.execute(sql)
                con.commit()
                
                
                rows = cursor.fetchall()
                
                #(rice, priceone, pricehalf, pricetwo) = rows[0]
                #print(startPageRice)
                
            except ValueError:
                answer_price.config(text="Not a number!! Please input a Number")
                onekg_entry.delete(0, END)
                halfkg_entry.delete(0, END)
                twokg_entry.delete(0, END)

class SeeTransactions(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        self.controller = controller

        #header
        TopFrame = Frame(self, bg=hf)
        TopFrame.grid(column=0, row=0, padx=(0, 0), sticky="nsew")
        TopFrame.grid_rowconfigure(0, weight=1)
        TopFrame.grid_columnconfigure(0, weight=1)
        
        #header label
        self.label1 = Label(TopFrame, text="See transactions",font =("Arial, 18"),bg = hf,fg ="#FF0000",width = 60,height = 2)
        self.label1.grid(column=0, row=0, sticky = "nsew")
        self.firstbutton = HoverButton(TopFrame,bg = hf,
                                       activebackground=hf,relief= "flat",
                                       highlightthickness=0,
                                       command=lambda: controller.show_frame(AdminPage))
        
        self.backbutton= ImageTk.PhotoImage(Image.open("back2.png"))
        self.firstbutton.config(image = self.backbutton, width=100, height=50)
        self.firstbutton.grid(column = 0, row = 0, sticky="w")

        #Darkgreen line Top
        TopFrameB = Frame(self, height = 10)
        TopFrameB.grid(column = 0, row =1)

        #Middle InfoFrame
        InfoFrame = Frame(self, bg=bgm)
        InfoFrame.grid(column = 0, row =2, sticky ="ew")

        #Middle Frame
                            
        MidFrame = Frame(InfoFrame)
        MidFrame.grid(column = 0, row =0, sticky ="n", pady=(0,0), padx=(0,0))
        MidFrame.configure(background = bgm )
           
        self.width = 25
        self.height = 2
        self.padx = (100,0)
        self.pady = 4

        #table header
        self.ID_header = Label(MidFrame, text="NO.", background="chartreuse3", width=15, height=1)
        self.ID_header.grid(column = 0, row=0, sticky="ew", padx=(0,0), pady=(0,0))
        
        self.date_time_header = Label(MidFrame, text="DATE&TIME", background="chartreuse3", width=15, height=1)
        self.date_time_header.grid(column = 1, row=0, sticky="ew", padx=(0,0), pady=(0,0))
        
        self.rice_header = Label(MidFrame, text="RICE", background="chartreuse3", width=15, height=1)
        self.rice_header.grid(column = 2, row=0, sticky="ew", padx=(0,0), pady=(0,0))        

        self.price_header = Label(MidFrame, text="PRICE", background="chartreuse3", width=15, height=1)
        self.price_header.grid(column = 3, row=0, sticky="ew", padx=(0,0), pady=(0,0))
        
        self.weight_header = Label(MidFrame, text="WEIGHT", background="chartreuse3", width=15, height=1)
        self.weight_header.grid(column = 4, row=0, sticky="ew", padx=(0,0), pady=(0,0))
        
        #table data
        
        global e
        con = sqlite3.connect('rice_vending_machine.db')
        cursor = con.cursor()
        sql = "SELECT * FROM transaction_logs ORDER BY id DESC LIMIT 10"
        cursor.execute(sql)
        con.commit()
        
        rows = cursor.fetchall()
        global e
        columnWidth=15
        i=1 # row value inside the loop
        j=0
        for row in rows:
            for data in row:
                columnWidth = 30 if j==1 else 15 #30 ang width kapag date and time

                e = Label(MidFrame, text=data, background="chartreuse3", width=columnWidth, height=1) 
                e.grid(row=i, column=j)
                j=j+1
            j=0
            i=i+1
        
        def updateTransactionsLog():
            con = sqlite3.connect('rice_vending_machine.db')
            cursor = con.cursor()
            sql = "SELECT * FROM transaction_logs ORDER BY id DESC LIMIT 10"
            cursor.execute(sql)
            con.commit()
            
            rows = cursor.fetchall()
            global e
            columnWidth=15
            i=1 # row value inside the loop
            j=0
            for row in rows:
                for data in row:
                    columnWidth = 30 if j==1 else 15 #30 ang width kapag date and time

                    e = Label(MidFrame, text=data, background="chartreuse3", width=columnWidth, height=1) 
                    e.grid(row=i, column=j)
                    j=j+1
                j=0
                i=i+1           
            self.after(1000, updateTransactionsLog)
            
        threading.Thread(target=updateTransactionsLog).start()
        
class StartPage(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        self.controller = controller
        
        #header
        TopFrame = Frame(self, bg=hf)
        TopFrame.grid(column=0, row=0, padx=(0, 0), sticky="nsew")
        TopFrame.grid_rowconfigure(0, weight=1)
        TopFrame.grid_columnconfigure(0, weight=1)
        
        #header label
        self.label1 = Label(TopFrame, text="PRICES",font =("Arial, 18"),bg = hf,width = 60,height = 2)
        self.label1.grid(column=0, row=0, sticky = "nsew")
        
        self.firstbutton = HoverButton(TopFrame,bg = hf,
                                       activebackground=hf,
                                       relief= "flat",
                                       highlightthickness=0,
                                       command=lambda:controller.show_frame(WelcomePage))
        self.backbutton= ImageTk.PhotoImage(Image.open
                                            ("back2.png"))
        self.firstbutton.config(image = self.backbutton, width=100, height=50)
        self.firstbutton.grid(column = 0, row = 0, sticky="w")

        #Darkgreen line Top
        TopFrameB = Frame(self, height = 10)
        TopFrameB.grid(column = 0, row =1)

        #Middle InfoFrame
        InfoFrame = Frame(self, bg=bgm)
        InfoFrame.grid(column = 0, row =2, sticky ="ew")

        global Mcontainer
        global Wcontainer
        global weight
        
        #Middle Frame
                                     
        MidFrame = Frame(InfoFrame)
        MidFrame.grid(column = 0, row =0, sticky ="n", pady=(20,15), padx=(45,0))
        MidFrame.configure(background = bgm )

        
        #MONEY
        self.Moneylabel = Label(MidFrame, background="chartreuse3", width="40", height=2)
        self.Moneylabel.grid(column = 0, row=2, sticky="nsew",padx=(15,0), pady=(20,0))
        self.transaclabel1 = Label(MidFrame, text="You have inserted:",bg="chartreuse3",fg= "yellow",font="sans-serif 22 bold",relief=GROOVE)
        self.transaclabel1.grid(column = 0, row=2, sticky="nsew" ,padx=(15,0), pady=(0,0))

        Mcontainer = Label(MidFrame,text=credit,background="linen", font="sans-serif 60 bold ")
        Mcontainer.grid(column = 0, row=4, sticky="nsew" ,padx=(15,0), pady=(0,0))

        
        #MONEY SIGN
        self.moneysign = Label(MidFrame, text="P",bg="linen",fg= "black",font="sans-serif 60 bold")
        self.moneysign.place(relx=0.05, rely=0.19)
        
        #WEIGHT
        self.Weightlabel = Label(MidFrame,background="chartreuse3",width=37,height=3,relief=RIDGE)
        self.Weightlabel.grid(column = 0, row=5, sticky="nsew",padx=(15,0), pady=(25,0))
        self.Weightlabel1 = Label(MidFrame,text="Available Weight:",background="chartreuse3",font="sans-serif 15 bold",fg="yellow")
        self.Weightlabel1.grid(column = 0, row=5, sticky="nsew",padx=(15,0), pady=(25,0))

        Wcontainer = Label(MidFrame,text=weight,background="linen",font="sans-serif 40 bold",width=2)
        Wcontainer.grid(column = 0, row=6, sticky="nsew" ,padx=(15,0), pady=(0,0))


        #Rice and Price

        global startPagePriceOneLabel
        global startPagePriceHalfLabel
        global startPagePriceTwoLabel
        global startPageRiceLabel
        
        global startPagePriceOne
        global startPagePriceHalf
        global startPagePriceTwo
        global startPageRice
        
        weight = getWeight()
        con = sqlite3.connect('rice_vending_machine.db')
        cursor = con.cursor()
        sql = "SELECT * FROM prices"
        cursor.execute(sql)
        con.commit()
        
        
        rows = cursor.fetchall()
        (startPageRice, startPagePriceOne, startPagePriceHalf, startPagePriceTwo) = rows[0]

        self.Ricelabel = Label(MidFrame, background="chartreuse3", width="40", height=2)
        self.Ricelabel.grid(column = 2, row=2, sticky="nsew",padx=(90,0), pady=(0,0))
        startPageRiceLabel = Label(MidFrame, text=startPageRice,bg="chartreuse3",fg= "yellow",font="sans-serif 25 bold",relief=GROOVE)
        startPageRiceLabel.grid(column = 2, row=2, sticky="nsew" ,padx=(90,0), pady=(0,0))

        self.tbprice = Label (MidFrame, text="PRICE", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        self.tbprice.place(relx=0.58, rely=0.20)

        self.tbweight = Label (MidFrame, text="WEIGHT", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        self.tbweight.place(relx=0.81, rely=0.20)

        self.yellowlabel = Label(MidFrame, text="", bg="yellow", height = 23, width =45)
        self.yellowlabel.place(relx=0.58, rely=0.27)

        #PRICES PRINT
        startPagePriceOneLabel = Label(MidFrame, text=startPagePriceOne, fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        startPagePriceOneLabel.place(relx=0.604, rely=0.35)

        startPagePriceHalfLabel = Label(MidFrame, text=startPagePriceHalf, fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        startPagePriceHalfLabel.place(relx=0.604, rely=0.55)

        startPagePriceTwoLabel = Label(MidFrame, text=startPagePriceTwo, fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        startPagePriceTwoLabel.place(relx=0.604, rely=0.75)


        #WEIGHT PRINT

        self.label1kg =Label(MidFrame, text="1 KG", fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        self.label1kg.place(relx=0.81, rely=0.35)

        self.label2kg =Label(MidFrame, text="1 1/2 KG", fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        self.label2kg.place(relx=0.81, rely=0.55)

        self.label3kg =Label(MidFrame, text="2 KG", fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        self.label3kg.place(relx=0.81, rely=0.75)


        
        
        #Dark Green line Bottom
        BottomFrame1 = Frame(self, height= 10)
        BottomFrame1.grid(column=0, row=3)

        
        #Footer
        BottomFrame = Frame(self, height=70, bg=hf)
        BottomFrame.grid(column=0, row=4, sticky ="ew")

        def order():
            global credit
            if (credit == int(startPagePriceOne)):
                if(getWeight() > 1):
                    messagebox.showinfo("ORDERED", "DISPENSING 1KG, PLEASE WAIT")
                    threading.Thread(target=dispenseOne).start()
                    insertTransactionLog(credit, "1kg")
                    credit = 0
                else:
                    messagebox.showinfo("WARNING", "INSUFFICIENT WEIGHT")
            elif (credit == int(startPagePriceHalf)):
                if(getWeight() > 1.5):
                    messagebox.showinfo("ORDERED", "DISPENSING 1.5KG, PLEASE WAIT")
                    threading.Thread(target=dispenseOneAndHalf).start()
                    insertTransactionLog(credit, "1.5kg")
                    credit = 0
                else:
                    messagebox.showinfo("WARNING", "INSUFFICIENT WEIGHT")
            elif (credit == int(startPagePriceTwo)):
                if(getWeight() > 2):
                    messagebox.showinfo("ORDERED", "DISPENSING 2KG, PLEASE WAIT")
                    threading.Thread(target=dispenseTwo).start()
                    insertTransactionLog(credit, "2kg")
                    credit = 0
                else:
                    messagebox.showinfo("WARNING", "INSUFFICIENT WEIGHT")
            else:
                messagebox.showinfo("WARNING", "INVALID AMOUNT")
                print("invalid amount")
            
            

        self.button=Button(BottomFrame, text="ORDER",width=7, command=order, bg="gray", fg="black", font="sans-serif 18 bold")
        self.button.place(rely=0.08, relx=0.4)
        
        
            
        def update():
            weight = getWeight()
            Mcontainer.configure(text=credit)
            Wcontainer.configure(text=weight)
            startPageRiceLabel.configure(text=startPageRice)
            startPagePriceOneLabel.configure(text=startPagePriceOne)
            startPagePriceHalfLabel.configure(text=startPagePriceHalf)
            startPagePriceTwoLabel.configure(text=startPagePriceTwo)
            self.after(10, update)
            

        threading.Thread(target=update).start()

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
        entry.insert('end', value)



def create(self, entry):

    window = Toplevel(self)
    window.configure(background=hf)
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


    
#Hover Button        
class HoverButton(tk.Button):
    def __init__(self, master, **k):
        Button.__init__(self, master=master, **k)
        self.defaultBackground = self["background"]
        self.highlightthickness = self["highlightthickness"]
        self.borderwidth = self["borderwidth"]
     
     

#BILL ACCEPTOR
credit=0

device0 = '/dev/ttyUSB0'
stadevice1 = '/dev/ttyUSB1'

def billAcceptor():
    serialbuffer = 0
    ser = None

    try:
        ser = serial.Serial(device0, 9600)
    except:
        try:
            ser = serial.Serial(device1, 9600)
        except Exception as ex:
                print(ex)
    
    while True:
        serialbuffer = ser.readline().decode("utf-8").lstrip().rstrip()
        global credit
        credit += int(serialbuffer)
        #print(credit)

#WEIGHT SENSOR

weight=0

EMULATE_HX711=False

referenceUnit = 1

if not EMULATE_HX711:
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
#hx.set_reference_unit(-113)
hx.reset()
hx.tare()
#print("Tare done! Add weight now...")

calibrationFactor = 26.6

def getWeight():
    val = max(0, hx.get_weight(5))
    kilogram = val/(1000*calibrationFactor)
    print(val/1000)
    return round(kilogram, 2) # round to 2 decimal places
    
    
# SERVO
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)
servo.start(0)
servo.ChangeDutyCycle(2)

def dispenseOne():   
    servo.start(0)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    servo.ChangeDutyCycle(7)
    time.sleep(1.49)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    print("One Kilo dispensed")
    
def dispenseOneAndHalf():
    servo.start(0)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    servo.ChangeDutyCycle(7)
    time.sleep(2.23)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    #servo.detach()
    servo.stop()
    print("One and half kilo dispensed")
    
def dispenseTwo():
    servo.start(0)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    servo.ChangeDutyCycle(7)
    time.sleep(3.2)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    #servo.detach()
    servo.stop()
    print("Two Kilo dispensed")
    
#insert transaction log
def insertTransactionLog(orderPrice, orderWeight):
    mydate = datetime.datetime.now()
    date_time = mydate.strftime("%B %d, %G %r")

    #Insert new transaction record
    con = sqlite3.connect('rice_vending_machine.db')
    cursor = con.cursor()
    sql = "INSERT INTO transaction_logs (date_time, rice, price, weight) VALUES (?,?,?,?)"
    cursor.execute(sql, (date_time, str(startPageRice), str(orderPrice), orderWeight))
    con.commit()
    

#THREADS
threading.Thread(target=billAcceptor).start()

app = VendingMachine()
app.title("Vending Machine")
app.geometry('800x480')
app.configure(background=dl)
app.resizable(0, 0)
app.attributes('-fullscreen',False)
app.mainloop()
    

