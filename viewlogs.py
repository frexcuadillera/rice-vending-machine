import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import sqlite3
from sqlite3 import Error
import math


# TKINTER FRAME
win = tk.Tk()
win.title('NFC-based Attendance Monitoring')
win.resizable(False, False)
##win.attributes('-fullscreen', True)
win.geometry("800x500")

# Logs
viewlogs__screen = tk.Label(win)
viewlogs__screenarea = tk.Label(win)
viewlogs__name = tk.Label(win)
viewlogs__floor = tk.Label(win)
viewlogs__status = tk.Label(win)
viewlogs__time = tk.Label(win)
viewlogs__nameData = tk.Label(win)
viewlogs__floorData = tk.Label(win)
viewlogs__statusData = tk.Label(win)
viewlogs__timeData = tk.Label(win)
viewlogs__buttonLeft = tk.Button(win)
viewlogs__buttonRight = tk.Button(win)
viewlogs__pagePanel = tk.Label(win)


# CONSTANTS
refreshTime = 100 #in milliseconds
screen = 'viewlogs'
# COLOR CODES
light__green = '#9cff80'
bright__yellow = '#fffd80'
light__yellow = '#ffffcc'
light__green2 = '#d1ffcc'
light__blue = '#4284f5'
light__blueHover = '#1C53B0'
light__red = '#ff8080'
light__grey = '#bab6b6'
light__grey2 = '#545454'
light__purple = '#b580ff'
light__orange = '#ffc080'
light__blue2 = '#97befc'
light__brown = '#deb887'
maroon = '#800000'
white = '#ffffff'
black = '#403d37'
black2 = '#2e2d2a'
dark__blue = '#1f2630'
dark__red = '#d40000'
dark__green = '#004d17'
dark__purple = '#9700a8'
prominence__blue = '#0049a3'
prominence__lightBlue = '#00a897'
prominence__darkBlue = '#002463'
prominence__green = '#00a83e'
prominence__red = '#a80000'
prominence__brown = '#5e1b00'
prominence__pink = '#fc034e'
blackest__green = '#003b23'
ridgel__red = '#ffbdbd'
ridgel__green = '#8aff75'
ridgel__blue = '#add6ff'
ridgel__purple = '#bc75ff'
ridgel__yellow = '#ffed75'


maxLogsPerPage = 20
page = 1

def viewlogs():
    con = sqlite3.connect('nfc.db')
    with con:
        cursor=con.cursor()
        sql = "SELECT * FROM data_logs "
        sql+= "INNER JOIN registered_users "
        sql+= "ON data_logs.UID = registered_users.UID "
        sql+= "WHERE data_logs.date < datetime('now', '+8 hour') "
        sql+= "AND data_logs.date > datetime('now', '-30 day', '+8 hour') "
        sql+= "ORDER BY data_logs.date DESC "
        cursor.execute(sql)
        
        con.commit()
        nameData = ""
        floorData = ""
        statusData = ""
        timeData = ""
        rows = cursor.fetchall()
        count = 0

        for row in rows:
            if (count>=maxLogsPerPage*(page-1) and count<maxLogsPerPage*page):
                nameData += row[6]+" "+row[7]+"\n"
                floorData += row[9]+"\n"
                statusData += row[2]+"\n"
                timeData += row[3]+"\n"
            count += 1

    maxPage = math.ceil(len(rows)/maxLogsPerPage)
    def backPage():
        global page
        page = max(1, page-1)

    def nextPage():
        global page
        page = min(page+1, maxPage)
  
    viewlogs__screen.place(relx = 0,
                         rely = 0,
                         relwidth = 1,
                         relheight = 1)
    viewlogs__screen.config(bg = black)
      
    viewlogs__screenarea.place(relx = 0.1,
                         rely = 0.15,
                         relwidth = 0.8,
                         relheight = 0.73)
    viewlogs__screenarea.config(bg = light__yellow)

    viewlogs__name.place(relx = 0.10,
                         rely = 0.05,
                         relwidth = 0.28,
                         relheight = 0.1)
    viewlogs__name.config(text = 'Tenant Name',
                              bg = light__brown,
                              fg = maroon,
                              font = ("Arial Bold",15))
    viewlogs__floor.place(relx = 0.38,
                         rely = 0.05,
                         relwidth = 0.12,
                         relheight = 0.1)
    viewlogs__floor.config(text = 'Floor No.',
                              bg = light__brown,
                              fg = maroon,
                              font = ("Arial Bold",15))
    viewlogs__status.place(relx = .50,
                         rely = 0.05,
                         relwidth = 0.15,
                         relheight = 0.1)
    viewlogs__status.config(text = 'Status',
                              bg = light__brown,
                              fg = maroon,
                              font = ("Arial Bold",15))                                                                                                                                              
    viewlogs__time.place(relx = 0.65,
                         rely = 0.05,
                         relwidth = 0.25,
                         relheight = 0.1)
    viewlogs__time.config(text = 'Date and Time',
                              bg = light__brown,
                              fg = maroon,
                              font = ("Arial Bold",15))
    #---------------  View Logs Data   --------------#
    viewlogs__nameData.place(relx = 0.10,
                         rely = 0.16,
                         relwidth = 0.30,
                         relheight = 0.72)
    viewlogs__nameData.config(text = nameData,
                              bg = light__yellow,
                              fg = dark__blue,
                              font = ("Arial",11),
                              anchor = 'n')
    viewlogs__floorData.place(relx = 0.40,
                         rely = 0.16,
                         relwidth = 0.10,
                         relheight = 0.72)
    viewlogs__floorData.config(text = floorData,
                              bg = light__yellow,
                              fg = dark__blue,
                              font = ("Arial",11),
                              anchor = 'n')
    viewlogs__statusData.place(relx = .50,
                         rely = 0.16,
                         relwidth = 0.15,
                         relheight = 0.72)
    viewlogs__statusData.config(text = statusData,
                              bg = light__yellow,
                              fg = dark__blue,
                              font = ("Arial",11),
                              anchor = 'n')                                                                                                                                              
    viewlogs__timeData.place(relx = 0.65,
                         rely = 0.16,
                         relwidth = 0.22,
                         relheight = 0.72)
    viewlogs__timeData.config(text = timeData,
                              bg = light__yellow,
                              fg = dark__blue,
                              font = ("Arial",11),
                              anchor = 'n')
    

    viewlogs__buttonLeft.place(relx = 0.38,
                               rely = 0.91,
                               width = 30,
                               height = 30)
    viewlogs__buttonLeft.config(text= '<',
                                bg = white,
                                fg = dark__blue,
                                relief = 'flat',
                                font = ('Calibri Bold', 25),
                                command = backPage)
    viewlogs__buttonRight.place(relx = 0.60,
                               rely = 0.91,
                               width = 30,
                               height = 30)
    viewlogs__buttonRight.config(text= '>',
                                bg = white,
                                fg = dark__blue,
                                relief = 'flat',
                                font = ('Calibri Bold', 25),
                                command = nextPage)
    viewlogs__pagePanel.place(relx = .43,
                              rely = 0.91,
                              width = 125,
                              height = 30)
    viewlogs__pagePanel.config(text = "Page %s/%s"%(page, maxPage),
                               bg = black,
                               fg = white,
                               font = ("Calibri Bold",14))

def screenChange__viewlogs():
    global screen
    screen = 'viewlogs'

def update():
    if(screen == 'viewlogs'):
        viewlogs()
    win.after(refreshTime, update)
win.after(refreshTime, update)
