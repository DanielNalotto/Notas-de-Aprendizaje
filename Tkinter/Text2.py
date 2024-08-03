from tkinter import *

# El primer Text está junto con el archivo de Scrollbar

root1 = Tk()

root2 = Tk()

root1.geometry('300x300')
root2.geometry('300x300')


def a():
    b = t1.get(1.0, END)
    t2.delete(1.0, END)
    t2.insert(1.0, b)


t1 = Text(root1)
t1.place(x=10, y =10, width=200, height=200)

b = Button(root1, text='aceptar', command=a)
b.place(x=80, y=240)

t2 = Text(root2)
t2.place(x=10, y =10, width=200, height=200)
