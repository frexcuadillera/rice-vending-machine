from tkinter import *
from PIL import ImageTk, Image
import os
import sys
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import threading
import RPi.GPIO as GPIO
import time
import serial



hf = '#74e216'  #header and footer
dl = '#306700'  #dark line
bgm = '#c0ea9d' #middle




class VendingMachine(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomePage, AdminLogin, AdminPage, AdminChangeAccount,
                  AdminChangePrice,StartPage, SeePrice):

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
        self.button2 = HoverButton(ButtonsFrame,
                                   bg =hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0,
                                   command=lambda: controller.show_frame(SeePrice))
        self.img1 = ImageTk.PhotoImage(Image.open("price2.png"))
        self.button2.config(image=self.img1, width = 310, height = 70)
        self.button2.grid(column = 0, row = 15,
                          padx = self.padx, pady = self.pady)
        

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
        with open("user.txt") as f:
            new = f.readlines()
            name = new[0].rstrip()
            password = new[1].rstrip()

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
        
        #Button 2
        self.button2 = HoverButton(ButtonsFrame,
                                   bg =hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0,
                                   command=lambda: controller.show_frame(AdminChangePrice))
        self.img1 = ImageTk.PhotoImage(Image.open("changeprices.png"))
        self.button2.config(image=self.img1, width = 310, height = 70)
        self.button2.grid(column = 0, row = 15,
                          padx = self.padx, pady = self.pady)
        

        #Button 3
        self.button3 = HoverButton(ButtonsFrame,
                                   bg =hf,
                                   activebackground=dl,
                                   relief= "flat",
                                   highlightthickness=0)
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
                data = username.get() + "\n" + password.get()

                with open("user.txt", "w") as f:
                    f.writelines(data)
                    f.close
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

        #login

        global rice
        global onekg
        global halfkg
        global twokg
        
        rice = StringVar()
        onekg = StringVar()
        halfkg = StringVar()
        twokg = StringVar()

        global rice_entry
        global onekg_entry
        global halfkg_entry
        global twokg_entry

        global answer_price

        placeholder_text = '0'

        self.rice = Label(MidFrame, text="Kind of Rice: * ", bg=bgm, font =("Arial, 14"))
        self.rice.grid(column=1, row=0, padx = self.padx , pady = 40)
        rice_entry = Entry(MidFrame, textvariable=rice, font =("Arial, 12"))
        rice_entry.grid(column = 2, row =0,padx = (20,0))
        sixthkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, rice_entry))
        sixthkey_button.grid(column =3, row=0)
        
        self.onekg = Label(MidFrame, text="1 Kg: * ", bg = bgm, font=("Arial, 14"))
        self.onekg.grid(column = 1, row = 2, padx = self.padx ,pady = self.pady)
        onekg_entry = Entry(MidFrame, textvariable=onekg,font =("Arial, 12"))
        onekg_entry.grid(column = 2, row = 2, padx= (20,0), pady = self.pady)
        onekg_entry.insert(0, placeholder_text)
        seventhkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, onekg_entry))
        seventhkey_button.grid(column =3, row=2)

        
        self.halfkg = Label(MidFrame, text="1 1/2 Kg: * ", bg = bgm, font=("Arial, 14"))
        self.halfkg.grid(column = 1, row = 3, padx = self.padx ,pady = self.pady)
        halfkg_entry = Entry(MidFrame, textvariable=halfkg,font =("Arial, 12"))
        halfkg_entry.grid(column = 2, row = 3, padx= (20,0), pady = self.pady)
        halfkg_entry.insert(0, placeholder_text)
        eightkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, halfkg_entry))
        eightkey_button.grid(column =3, row=3)
        

        self.twokg = Label(MidFrame, text="2 Kg: * ", bg = bgm, font=("Arial, 14"))
        self.twokg.grid(column = 1, row = 4, padx = self.padx ,pady = self.pady)
        twokg_entry = Entry(MidFrame, textvariable=twokg,font =("Arial, 12"))
        twokg_entry.grid(column = 2, row = 4, padx= (20,0), pady = self.pady)
        twokg_entry.insert(0, placeholder_text)
        ninthkey_button = Button(MidFrame, text='Keyboard', bg=bgm, command=lambda:create(self, twokg_entry))
        ninthkey_button.grid(column =3, row=4)
        

        answer_price = Label(MidFrame, text="", bg = bgm, fg = "red")
        answer_price.grid(column = 2, row = 5)


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
        
        if len(rice.get()) == 0 or len(onekg.get())==1 or len(halfkg.get())==1 or len(twokg.get())==1:
            answer_price.config(text="Fields must be filled in")
        else:
            try:
                int(onekg.get())
                int(halfkg.get())
                int(twokg.get())
                data = rice.get() + "\n" + str(onekg.get()) + "\n" + str(halfkg.get()) + "\n" + str(twokg.get())

                with open("Price.txt", "w") as f:
                    f.writelines(data)
                    f.close()
                rice_entry.delete(0, END)
                onekg_entry.delete(0, END)
                halfkg_entry.delete(0, END)
                twokg_entry.delete(0, END)
                answer_price.config(text="")
                self.controller.show_frame(AdminPage)
                messagebox.showinfo("SUCCESSFUL", "Successfully changed!")

                #THIS IS FOR THE DISPLAY OF DATA IN SEE PRICE PAGE
                with open("Price.txt","r") as f:
                    new = f.readlines()
                    rice1 = new[0].rstrip()
                    priceone = new[1].rstrip()
                    pricehalf = new[2].rstrip()
                    pricetwo = new[3].rstrip()
                    f.close()
                label6.config(text=rice1)
                label7.config(text=priceone)
                label8.config(text=pricehalf)
                label9.config(text=pricetwo)

                transaclabel.config(text=rice1)
                labelprice.config(text=priceone)
                labelprice1.config(text=pricehalf)
                labelprice2.config(text=pricetwo)
                
            except ValueError:
                answer_price.config(text="Not a number!! Please input a Number")
                onekg_entry.delete(0, END)
                halfkg_entry.delete(0, END)
                twokg_entry.delete(0, END)


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

        global labelprice
        global labelprice1
        global labelprice2
        global transaclabel


        with open("Price.txt","r") as f:
            new = f.readlines()
            rice1 = new[0].rstrip()
            priceone = new[1].rstrip()
            pricehalf = new[2].rstrip()
            pricetwo = new[3].rstrip()
            f.close()
        
        self.Ricelabel = Label(MidFrame, background="chartreuse3", width="40", height=2)
        self.Ricelabel.grid(column = 2, row=2, sticky="nsew",padx=(90,0), pady=(0,0))
        transaclabel = Label(MidFrame, text=rice1,bg="chartreuse3",fg= "yellow",font="sans-serif 25 bold",relief=GROOVE)
        transaclabel.grid(column = 2, row=2, sticky="nsew" ,padx=(90,0), pady=(0,0))

        self.tbprice = Label (MidFrame, text="PRICE", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        self.tbprice.place(relx=0.58, rely=0.20)

        self.tbweight = Label (MidFrame, text="WEIGHT", bg="chartreuse3", fg="black", font="sans-serif 12 bold", width="14")
        self.tbweight.place(relx=0.81, rely=0.20)

        self.yellowlabel = Label(MidFrame, text="", bg="yellow", height = 23, width =45)
        self.yellowlabel.place(relx=0.58, rely=0.27)

        #PRICES PRINT
        labelprice = Label(MidFrame, text=priceone, fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        labelprice.place(relx=0.604, rely=0.35)

        labelprice1 = Label(MidFrame, text=pricehalf, fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        labelprice1.place(relx=0.604, rely=0.55)

        labelprice2 = Label(MidFrame, text=pricetwo, fg="black", bg ="yellow",font="sans-serif 12 bold", width="14")
        labelprice2.place(relx=0.604, rely=0.75)


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
            if (credit == int(priceone)):       
                threading.Thread(target=dispenseOne).start()
                credit = 0
            elif (credit == int(pricehalf)):
                threading.Thread(target=dispenseOneAndHalf).start()
                credit = 0
            elif (credit == int(pricetwo)):
                threading.Thread(target=dispenseTwo).start()
                credit = 0
            else:
                print("invalid amount")
            
            

        self.button=Button(BottomFrame, text="ORDER",width=7, command=order, bg="gray", fg="black", font="sans-serif 18 bold")
        self.button.place(rely=0.08, relx=0.4)
        
        
            
        def update():
            weight = getWeight()
            Mcontainer.configure(text=credit)
            Wcontainer.configure(text=weight)
            self.after(10, update)
           

        threading.Thread(target=update).start()

class SeePrice(Frame):
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

        #Middle Frame
                                     
        MidFrame = Frame(InfoFrame)
        MidFrame.grid(column = 0, row =0, sticky ="n", pady=(20,15), padx=(60,0))
        MidFrame.configure(background = bgm )

        global label6
        global label7
        global label8
        global label9

        with open("Price.txt","r") as f:
            new = f.readlines()
            rice1 = new[0].rstrip()
            priceone = new[1].rstrip()
            pricehalf = new[2].rstrip()
            pricetwo = new[3].rstrip()
            f.close()
            
        #SEE PRICES LABELS
        self.label2 = Label(MidFrame, text="Rice:", font=("Arial, 16"), width=10,bg=dl, fg="white")
        self.label2.grid(column = 0, row=4, sticky="nsew" ,padx=(45,0), pady=(0,0))

        self.label3 = Label(MidFrame, text="1 Kilo:", font=("Arial, 16"),width=10, bg=dl, fg="white")
        self.label3.grid(column = 2, row=0, sticky="nsew" ,padx=(200,0), pady=(0,10))

        self.label4 = Label(MidFrame, text="1 1/2 Kilo:", font=("Arial, 16"),width=10, bg=dl, fg="white")
        self.label4.grid(column = 2, row=4, sticky="nsew" ,padx=(200,0), pady=(0, 10))

        self.label5 = Label(MidFrame, text="2 Kilo:", font=("Arial, 16"),width=10, bg=dl, fg="white")
        self.label5.grid(column = 2, row=8, sticky="nsew" ,padx=(200,0), pady=(0,10))


        label6 = Label(MidFrame, text=rice1, font=("Arial, 42"),bg=bgm)
        label6.grid(column = 0, row=6, sticky="nsew" ,padx=(45,0), pady=(0,0))

        
        label7 = Label(MidFrame, text=priceone, font=("Arial, 24"),bg=bgm)
        label7.grid(column = 2, row=2, sticky="nsew" ,padx=(200,0), pady=(0,10))

        label8 = Label(MidFrame, text=pricehalf, font=("Arial, 24"),bg=bgm)
        label8.grid(column = 2, row=6, sticky="nsew" ,padx=(200,0), pady=(0,10))

        label9 = Label(MidFrame, text=pricetwo, font=("Arial, 24"),bg=bgm)
        label9.grid(column = 2, row=10, sticky="nsew" ,padx=(200,0), pady=(0,10))

        #Dark Green line Bottom
        BottomFrame1 = Frame(self, height= 10)
        BottomFrame1.grid(column=0, row=3)

        #Footer
        BottomFrame = Frame(self, height=70, bg=hf)
        BottomFrame.grid(column=0, row=4, sticky ="ew")

        


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
hx.set_reference_unit(-113)
hx.reset()
hx.tare()
#print("Tare done! Add weight now...")

def getWeight():
    val = max(0, hx.get_weight(5))
    kilo =(val/1000)
    weight = ("{:.0f}".format(kilo))
    return weight
    
# SERVO
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)

def dispenseOne():   
    servo.start(0)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    servo.ChangeDutyCycle(7)
    time.sleep(1.49)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    #servo.detach()
    print("One Kilo dispensed")
    
def dispenseOneAndHalf():
    servo.start(0)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    servo.ChangeDutyCycle(7)
    time.sleep(2.23)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    servo.detach();
    print("One and half kilo dispensed")
    
def dispenseTwo():
    servo.start(0)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    servo.ChangeDutyCycle(7)
    time.sleep(3.2)
    servo.ChangeDutyCycle(2)
    time.sleep(.5)
    servo.detach();
    print("Two Kilo dispensed")

#THREADS
threading.Thread(target=billAcceptor).start()

app = VendingMachine()
app.title("Vending Machine")
app.geometry('800x480')
app.configure(background=dl)
app.resizable(0, 0)
app.attributes('-fullscreen',False)
app.mainloop()
    
