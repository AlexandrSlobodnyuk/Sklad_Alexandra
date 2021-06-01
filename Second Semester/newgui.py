from tkinter import *

def gcd(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if a == 0 and b != 0:
        return b
    if b == 0 and a != 0:
        return a
    if a == 0 and b == 0:
        return 0

    r = int
    while r != 0:
        if a < b:
            z = a
            a = b
            b = z
        r = a % b
        a = r
    return b


def clicked1():
    res = str(txt1.get())
    lbl.configure(text = res)

def clicked2():
    res = str(txt2.get())
    lbl.configure(text= res)
def obrabotka():
    try:
        n1 = int(txt1.get())
        n2 = int(txt2.get())
        u = gcd(n1, n2)
        lbl.configure(text='Ur gcd is ' + str(u))
    except:
        lbl.configure(text='Input integer numbers')

window = Tk()
window.title("Наибольший общий делитель")
window.geometry('200x150')
lbl = Label(window, text="Привет")
txt1 = Entry(window, width = 10)
txt2 = Entry(window, width = 10)
#btn1 = Button(window, text = 'insert', command = clicked1)
#btn2 = Button(window,text = 'insert', command = clicked2)
btn3 = Button(window, text= 'find the gcd', command = obrabotka)


lbl.grid(column=0, row=0)


txt1.grid(column = 0, row = 1)
txt2.grid(column = 0, row =2)
#btn1.grid(column = 1,row = 1)
#btn2.grid(column = 1, row =2)
btn3.grid(column = 3, row = 2)

window.mainloop()
