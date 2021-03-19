import tkinter as tk
from tkinter import ttk


#main function
exp = " "
def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)


def clear():
    global exp
    exp = " "
    equation.set(exp)

def enter():
    global exp
    exp = "Next Line: "
    equation.set(exp)





key = tk.Tk()
key.title("Keyboard")
key.geometry("800x130")
#key.resizable(False,False)
key.configure(background="dodger blue")


equation = tk.StringVar()
##dis_entry = ttk.Entry(key, state = "readonly", textvariable = equation )
##dis_entry.grid(rowspan=1, columnspan=100, ipadx=999,ipady=20)


#Buttons
q = ttk.Button(key,text = 'Q', command = lambda : press('Q'))
q.place(relx=0, rely=0)

w = ttk.Button(key,text = 'W', command = lambda : press('W'))
w.place(relx=0.10, rely=0)

e = ttk.Button(key,text = 'E', command = lambda : press('E'))
e.place(relx=0.20, rely=0)

r = ttk.Button(key,text = 'R', command = lambda : press('R'))
r.place(relx=0.30, rely=0)

t = ttk.Button(key,text = 'T', command = lambda : press('T'))
t.place(relx=0.40, rely=0)

y = ttk.Button(key,text = 'Y', command = lambda : press('Y'))
y.place(relx=0.50, rely=0)

u = ttk.Button(key,text = 'U', command = lambda : press('U'))
u.place(relx=0.60, rely=0)

i = ttk.Button(key,text = 'I', command = lambda : press('I'))
i.place(relx=0.70, rely=0)

o = ttk.Button(key,text = 'O', command = lambda : press('O'))
o.place(relx=0.80, rely=0)

p = ttk.Button(key,text = 'P', command = lambda : press('P'))
p.place(relx=0.90, rely=0)

def clear():
    pass

Clr = ttk.Button(key,text = 'Clear', command = clear)
Clr.place(relx=0.90, rely=0.20)

a = ttk.Button(key,text = 'A', command = lambda : press('A'))
a.place(relx=0, rely=0.20)

s = ttk.Button(key,text = 'S', command = lambda : press('S'))
s.place(relx=0.10, rely=0.20)

d = ttk.Button(key,text = 'D', command = lambda : press('D'))
d.place(relx=0.20, rely=0.20)

f = ttk.Button(key,text = 'F', command = lambda : press('F'))
f.place(relx=0.30, rely=0.20)

g = ttk.Button(key,text = 'G', command = lambda : press('G'))
g.place(relx=0.40, rely=0.20)

h= ttk.Button(key,text = 'H', command = lambda : press('H'))
h.place(relx=0.50, rely=0.20)

j = ttk.Button(key,text = 'J', command = lambda : press('J'))
j.place(relx=0.60, rely=0.20)

k = ttk.Button(key,text = 'K', command = lambda : press('K'))
k.place(relx=0.70, rely=0.20)

l = ttk.Button(key,text = 'L', command = lambda : press('L'))
l.place(relx=0.80, rely=0.20)

def enter():
    pass
    
enter = ttk.Button(key,text = 'Enter', command = enter, width=30)
enter.place(relx=0.75, rely=0.40)

z = ttk.Button(key,text = 'Z', command = lambda : press('Z'))
z.place(relx=0, rely=0.40)

x = ttk.Button(key,text = 'X', command = lambda : press('X'))
x.place(relx=0.10, rely=0.40)

c = ttk.Button(key,text = 'C', command = lambda : press('C'))
c.place(relx=0.20, rely=0.40)

v = ttk.Button(key,text = 'V', command = lambda : press('V'))
v.place(relx=0.30, rely=0.40)

b = ttk.Button(key,text = 'B', command = lambda : press('B'))
b.place(relx=0.40, rely=0.40)

n = ttk.Button(key,text = 'N', command = lambda : press('N'))
n.place(relx=0.50, rely=0.40)

m = ttk.Button(key,text = 'M', command = lambda : press('M'))
m.place(relx=0.60, rely=0.40)
##################
k1 = ttk.Button(key,text = '1', command = lambda : press('1'))
k1.place(relx=0, rely=0.60)

k2 = ttk.Button(key,text = '2', command = lambda : press('2'))
k2.place(relx=0.10, rely=0.60)

k3 = ttk.Button(key,text = '3', command = lambda : press('3'))
k3.place(relx=0.20, rely=0.60)

k4 = ttk.Button(key,text = '4', command = lambda : press('4'))
k4.place(relx=0.30, rely=0.60)

k5 = ttk.Button(key,text = '5', command = lambda : press('5'))
k5.place(relx=0.40, rely=0.60)

k6 = ttk.Button(key,text = '6', command = lambda : press('6'))
k6.place(relx=0.50, rely=0.60)

k7 = ttk.Button(key,text = '7', command = lambda : press('7'))
k7.place(relx=0.60, rely=0.60)

k8 = ttk.Button(key,text = '8', command = lambda : press('8'))
k8.place(relx=0.70, rely=0.60)

k9 = ttk.Button(key,text = '9', command = lambda : press('9'))
k9.place(relx=0.80, rely=0.60)

k0 = ttk.Button(key,text = '0', command = lambda : press('0'))
k0.place(relx=0.90, rely=0.60)

##def space():
##    pass
##space = ttk.Button(key,text = 'Space', command = space, width=50)
##space.place(relx=0.20, rely=0.80)
key.mainloop()
