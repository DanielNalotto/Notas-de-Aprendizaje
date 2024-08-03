from tkinter import Tk
from tkinter import Checkbutton
from tkinter import IntVar
from tkinter import Button
from tkinter import messagebox
from tkinter import Entry
from tkinter import Label
from tkinter import DISABLED
from tkinter import StringVar
import sqlite3

def buscar():

    miConex=sqlite3.connect('Prueba1')
    miCursor=miConex.cursor()

    miCursor.execute("Select * from PERSONAJES where NOMBRE='" + nombre.get() + "'")
    lista=miCursor.fetchall()

    for l in lista:
        nombre.set(l[0])
        bot.set(l[1])  

def limpiar():
    bot.set(0)

root=Tk()

nombre=StringVar()
bot=IntVar()

l1=Label(root, text='Nombre:')
l1.place(x=10, y=10)

e1=Entry(root, textvariable=nombre)
e1.place(x=80, y=10)

c1=Checkbutton(root, text='Seleccionador', onvalue=1, offvalue=0, variable=bot, state=DISABLED)
c1.place(x=40, y=40)

b1=Button(root,text='Cargar', command=buscar, width=10)
b1.place(x=130, y=85)

b2=Button(root,text='Vaciar', command=limpiar, width=10)
b2.place(x=10, y=85)

root.geometry('220x130')
root.mainloop()
