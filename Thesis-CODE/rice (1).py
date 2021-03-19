import tkinter as tk


########## CONFIG ##########

# TKINTER FRAME
win = tk.Tk()
win.title('Automated Rice Vending Machine')
win.resizable(False, False)
win.attributes("-fullscreen", True)
win.geometry("800x480")

EMULATE_HX711=False

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711
hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(-113)
hx.reset()

hx.tare()

print("Tare done! Add weight now...")
def sense():
    try:
        val = max(0, int(hx.get_weight(5)))
        kilo =(val/1000)
        weight = ("{:.0f}".format(kilo))
        print(weight)
        return weight
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
        return 0
 


# CONSTANTS
refreshTime = 1000 #in milliseconds
screen = 'start'


# COLOR CODES
green = '#00aa00'
yellow = '#ffff00'
black = '#111111'
white = '#ffffff'
gray = '#dddddd'



########## SCREEN COMPONENTS ##########

# START SCREEN
start__topPanel = tk.Label(win)
start__adminButton = tk.Button(win)
start__newOwnerButton = tk.Button(win)
start__startButton = tk.Button(win)
start__bottomPanel = tk.Label(win)
start__powerButton = tk.Button(win)

# LOGIN SCREEN
login__topPanel = tk.Label(win)
login__userLabel = tk.Label(win)
login__userInput = tk.Entry(win)
login__passLabel = tk.Label(win)
login__passInput = tk.Entry(win)
login__bottomPanel = tk.Label(win)
login__loginButton = tk.Button(win)
login__cancelButton = tk.Button(win)

# ORDER SCREEN
order__topPanel = tk.Label(win)
order__insertLabel = tk.Label(win)
order__insertDisplay = tk.Label(win)
order__riceBrandLabel = tk.Label(win)
order__listHeader = tk.Label(win)
order__list = tk.Label(win)
order__bottomPanel =  tk.Label(win)
order__orderButton = tk.Button(win)

########## SCREENS ##########

# START SCREEN
def start():
    start__topPanel.place(relx = 0,
                          rely = 0,
                          relwidth = 1,
                          relheight = 0.15)
    start__topPanel.config(text = 'Automated Rice Vending Machine',
                           bg = green,
                           fg = yellow,
                           font = 20)
    start__adminButton.place(relx = 0.3,
                             rely = 0.2,
                             relwidth = 0.4,
                             relheight = 0.1)
    start__adminButton.config(text = 'Administrator',
                              bg = green,
                              font = 20,
                              command = screenChange__login)
    start__newOwnerButton.place(relx = 0.3,
                                rely = 0.4,
                                relwidth = 0.4,
                                relheight = 0.1)
    start__newOwnerButton.config(text = 'New Owner',
                                 bg = green,
                                 font = 20)
    start__startButton.place(relx = 0.3,
                             rely = 0.6,
                             relwidth = 0.4,
                             relheight = 0.1)
    start__startButton.config(text = 'Start',
                              bg = green,
                              font = 20,
                              command = screenChange__order)
    start__bottomPanel.place(relx = 0,
                             rely = 0.85,
                             relwidth = 1,
                             relheight = 0.15)
    start__bottomPanel.config(bg = green)
    start__powerButton.place(relx = 0.02,
                             rely = 0.87,
                             relwidth = 0.11,
                             relheight = 0.11)
    start__powerButton.config(bg = black)


# LOGIN SCREEN
def login():
    login__topPanel.place(relx = 0,
                    rely = 0,
                    relwidth = 1,
                    relheight = 0.15)
    login__topPanel.config(text = 'Please enter details below to login',
                           bg = green,
                           fg = yellow,
                           font = 20)
    login__userLabel.place(relx = 0.25,
                           rely = 0.25,
                           relwidth = 0.15,
                           relheight = 0.1)
    login__userLabel.config(text = 'Username',
                            bg = green,
                            fg = black,
                            font = 20)
    login__userInput.place(relx = 0.42,
                           rely = 0.25,
                           relwidth = 0.3,
                           relheight = 0.1)
    login__userInput.config(bg = white,
                            fg = black,
                            font = 20)
    login__passLabel.place(relx = 0.25,
                           rely = 0.4,
                           relwidth = 0.15,
                           relheight = 0.1)
    login__passLabel.config(text = 'Password',
                            bg = green,
                            fg = black,
                            font = 20)
    login__passInput.place(relx = 0.42,
                           rely = 0.4,
                           relwidth = 0.3,
                           relheight = 0.1)
    login__passInput.config(bg = white,
                            fg = black,
                            font = 20)
    login__bottomPanel.place(relx = 0,
                             rely = 0.85,
                             relwidth = 1,
                             relheight = 0.15)
    login__bottomPanel.config(bg = green)
    login__cancelButton.place(relx = 0.25,
                              rely = 0.87,
                              relwidth = 0.2,
                              relheight = 0.11)
    login__cancelButton.config(text = 'Cancel',
                               bg = gray,
                               fg = black,
                               font = 20,
                               command = screenChange__start)
    login__loginButton.place(relx = 0.52,
                             rely = 0.87,
                             relwidth = 0.2,
                             relheight = 0.11)
    login__loginButton.config(text = 'Login',
                              bg = gray,
                              fg = black,
                              font = 20)

# ORDER SCREEN
def order():
    order__topPanel.place(relx = 0,
                          rely = 0,
                          relwidth = 1,
                          relheight = 0.15)
    order__topPanel.config(text = 'Automated Rice Vending Machine',
                           bg = green,
                           fg = yellow,
                           font = 20)
    order__insertLabel.place(relx = 0.2,
                             rely = 0.23,
                             relwidth = 0.28,
                             relheight = 0.1)
    order__insertLabel.config(text = 'You have inserted',
                              bg = green,
                              fg = black,
                              font = 20)
    order__insertDisplay.place(relx = 0.2,
                               rely = 0.33,
                               relwidth = 0.28,
                               relheight = 0.4)
    order__insertDisplay.config(text = 'P50.00',
                                bg = white,
                                fg = black,
                                font = 20)
    order__riceBrandLabel.place(relx = 0.52,
                                rely = 0.23,
                                relwidth = 0.28,
                                relheight = 0.1)
    order__riceBrandLabel.config(text = 'Angelica',
                                 bg = green,
                                 fg = yellow,
                                 font = 20)
    order__listHeader.place(relx = 0.52,
                            rely = 0.33,
                            relwidth = 0.28,
                            relheight = 0.08)
    order__listHeader.config(text = 'Price\t\tWeight',
                             bg = green,
                             fg = black,
                             font = 20,
                             justify = 'left')
    order__list.place(relx = 0.52,
                      rely = 0.41,
                      relwidth = 0.28,
                      relheight = 0.32)
    order__list.config(text = '''P50.00\t\t1 kg
                               \nP80.00\t\t1 1/2 kg
                               \nP100.00\t\t 2 kg''',
                       bg = yellow,
                       fg = black,
                       font = 20,
                       justify = 'left')
    order__bottomPanel.place(relx = 0,
                             rely = 0.85,
                             relwidth = 1,
                             relheight = 0.15)
    order__bottomPanel.config(bg = green)
    order__orderButton.place(relx = 0.4,
                             rely = 0.87,
                             relwidth = 0.2,
                             relheight = 0.11)
    order__orderButton.config(text = 'Order',
                              bg = gray,
                              fg = black,
                              font = 20)


########## FUNCTIONS ##########

# CHANGE SCREEN FUNCTIONS

def screenChange__start():
    global screen
    screen = 'start'

def screenChange__login():
    global screen
    screen = 'login'

def screenChange__order():
    import Customer
#    global screen
#    screen = 'order'


# INTERFACE FUNCTIONS

def clear():
    start__topPanel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    start__adminButton.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    start__newOwnerButton.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    start__startButton.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    start__bottomPanel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    start__powerButton.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)

    login__topPanel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    login__userLabel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    login__userInput.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    login__passLabel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    login__passInput.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    login__bottomPanel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    login__loginButton.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    login__cancelButton.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)

    order__topPanel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__insertLabel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__insertDisplay.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__riceBrandLabel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__listHeader.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__list.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__bottomPanel.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)
    order__orderButton.place(relx = 0, rely = 0, relwidth = 0, relheight = 0)


def update():
    clear()
    
    if (screen == 'start'):
        start()
    elif (screen == 'login'):
        login()
    elif (screen == 'order'):
        order()
     
    weight = sense()
    order__insertDisplay.config(text = weight,
                                bg = white,
                                fg = black,
                                font = 20)
    
    win.after(refreshTime, update)
win.after(refreshTime, update)

