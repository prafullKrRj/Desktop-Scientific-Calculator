from tkinter import *
from tkinter import messagebox as msg
import math
from math import sin
from math import radians as r
from math import tan
from math import cos
root = Tk()
root.title('Calculator SSMP')
root.maxsize(513, 450)
root.minsize(513, 450)


colours = ["white", "gray85", "gray100", "gray100", "DarkOrange1", "gray20", "white", "black"]


def clear():
    var1.set("")
    screen.update()
def te():
    try:
        new_value = eval(screen.get())
    except:
        new_value = "Math Error!!"
    return new_value

def numbers(no, rowno, columnno, xpadding, comm):
    global frame
    Button(frame, text=f'{no}', bg=f"{colours[3]}", fg=f"{colours[7]}", font="cambria 25", padx=xpadding, relief=SUNKEN,
           command=comm).grid(row=rowno, column=columnno)

def operations(symbol, rowno, columnno, xpadding, comm):
    global frame
    Button(frame, text=f'{symbol}', bg=f"{colours[2]}", fg=f"{colours[7]}", font="cambria 25", padx=xpadding,
           relief=SUNKEN, command=comm).grid(row=rowno, column=columnno)

a = "Math Error!!"
def click(value):
    global frame
    try:
        l = ['=', 'π', 'math.factorial(', 'abs(', '1/x', 'e^x', 'e', 'x^y', 'sin', 'cos', 'tan']
        if value not in l:
            screen.insert(END, value)
        if value == 'C':
            clear()
        elif value == '=':
            if var1.get().isdigit():
                new_value = int(var1.get())
            else:
                new_value = te()
            var1.set(new_value)
            screen.update()
        elif value == 'π':
            screen.insert(END, 3.14159265359)
        elif value == 'math.factorial(':
            var1.set(math.factorial(eval(var1.get())))
        elif value == 'abs(':
            var1.set(abs(eval(var1.get())))
        elif value == '1/x':
            if eval(var1.get()) != 0:
                var1.set(1 / eval(var1.get()))
            else:
                var1.set(a)
        elif value == 'e^x':
            var1.set(math.e ** eval(var1.get()))
        elif value == 'e':
            screen.insert(END, math.e)
        elif value == 'x^y':
            screen.insert(END, '**')
    except:
        var1.get(a)

# keys
def enter(event):
    var1.set(te())

def keyboard(event):
    try:
        if event.char == '=':
            var2 = str(var1.get())
            var2 = var2[0: len(var2) - 1]
            try:
                new_value = eval(var2)
            except:
                new_value = a
            var1.set(new_value)
        if event.char == 'C' or event.char == 'c':
            clear()
        if event.char.isalpha():
            b = str(var1.get())
            var1.set(b[0:len(b) - 1])
    except:
        var1.set(0, "Math Error")

# Frame
frame = Frame(root, borderwidth=5, relief=SUNKEN, bg="grey")
frame.pack(anchor="nw", side=BOTTOM, fill=X)
# numbers
operations('C', 1, 2, 14.7, lambda: click('C'))
numbers(7, 2, 2, 15, lambda: click(7))
numbers(4, 3, 2, 15, lambda: click(4))
numbers(1, 4, 2, 15, lambda: click(1))
numbers('π', 5, 2, 14.5, lambda: click('π'))
numbers(8, 2, 3, 15, lambda: click(8))
numbers(5, 3, 3, 15, lambda: click(5))
numbers(2, 4, 3, 15, lambda: click(2))
numbers(0, 5, 3, 15, lambda: click(0))
operations('x²', 1, 3, 10, lambda: click('**2'))
numbers(9, 2, 4, 15, lambda: click(9))
numbers(6, 3, 4, 15, lambda: click(6))
numbers(3, 4, 4, 15, lambda: click(3))
numbers('.', 5, 4, 20, lambda: click('.'))
operations('√x', 1, 4, 4.5, lambda: click('**0.5'))
operations('÷', 1, 5, 22, lambda: click('/'))
operations('x', 2, 5, 22.5, lambda: click('*'))
operations('-', 3, 5, 26.4, lambda: click('-'))
operations('+', 4, 5, 22.5, lambda: click('+'))
operations('log', 1, 6, 14, lambda: click('math.log('))
operations('sin', 2, 6, 14.5, lambda: click('sin(r('))
operations('cos', 3, 6, 12, lambda: click('cos(r('))
operations('tan', 4, 6, 12.5, lambda: click('tan(r('))
operations('x^y', 5, 6, 10, lambda: click('x^y'))
operations('|x|', 1, 1, 18.5, lambda: click('abs('))
operations('e^x', 2, 1, 11.5, lambda: click('e^x'))
operations('e', 3, 1, 28, lambda: click('e'))
operations('n!', 4, 1, 23.49, lambda: click('math.factorial('))
operations('1/x', 5, 1, 12, lambda: click('1/x'))
Button(frame, text='=', bg=f"{colours[7]}", fg=f"{colours[0]}", font="cambria 25", padx=22, relief=SUNKEN,
       command=lambda: click("=")).grid(row=5, column=5)
var1 = StringVar()
screen = Entry(root, textvariable=var1, font="cambria 20", bg=f"{colours[0]}" , fg=f"{colours[7]}", relief=SUNKEN,
               justify=RIGHT)
screen.place(x=0, y=0, width=513, height=105)
root.bind('<Return>', enter)
root.bind('<Key>', keyboard)
root.mainloop()

