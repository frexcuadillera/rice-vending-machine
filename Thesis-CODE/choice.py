from tkinter import *
import serial


def ok():
    choice_screen.destroy()

    import current_time
    

def choice():
    
    global choice_screen
    choice_screen = Tk()
    choice_screen.title("Transaction")
    choice_screen.geometry("800x480")
    choice_screen.attributes("-fullscreen",True)

    label0 = Label (choice_screen, background="limegreen", width="100", height=80)
    label0.place(relx=0, rely= 0)

    label3 = Label(choice_screen, text="Thank You!",bg='limegreen',fg='white', font="Sans-serif 50 ")
    label3.place(relx=0.25, rely= 0.25)
    label4 = Label(choice_screen, text="(CLICK OK TO FINISH)",bg="limegreen", fg="forestgreen",font="Sans-serif 15 bold")
    label4.place(relx=0.33, rely= 0.42)
    button1 = Button(choice_screen, text="OK",fg='white',bg='darkgreen',width=18,height=2,font="Sans-serif 20 bold", command=ok)
    button1.place(relx=0.26, rely= 0.7)
#    choice_screen.mainloop()
#choice()
    
