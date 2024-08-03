from tkinter import Tk
from tkinter import Checkbutton
from tkinter import IntVar
from tkinter import Button
from tkinter import messagebox
from tkinter import Entry
from tkinter import Label
from tkinter import StringVar
import sqlite3

def guardar():
    miConex=sqlite3.connect('Prueba1')
    miCursor=miConex.cursor()

    try:
        miCursor.execute('create table PERSONAJES(NOMBRE varchar(20), BOT integer)')
        miCursor.commit()
        messagebox.showinfo('Prueba','Se ha creado la tabla con éxito.')
    except:
        pass

    try:
        miCursor.execute("insert into PERSONAJES values('" + nombre.get() + "','" + str(bot.get()) + "')")
                         
        miConex.commit()
        messagebox.showinfo('Prueba','Se han ingresado los datos a la tabla con éxito.')
    except:
        messagebox.showerror('Prueba','No se han ingresado los datos a la tabla.')

    

def limpiar():
    bot.set(0)

root=Tk()

nombre=StringVar()
bot=IntVar()

l1=Label(root, text='Nombre:')
l1.place(x=10, y=10)

e1=Entry(root, textvariable=nombre)
e1.place(x=80, y=10)

c1=Checkbutton(root, text='Seleccionador', onvalue=1, offvalue=0, variable=bot)
c1.place(x=40, y=40)

b1=Button(root,text='Aceptar', command=guardar, width=10)
b1.place(x=130, y=85)

b2=Button(root,text='Vaciar', command=limpiar, width=10)
b2.place(x=10, y=85)

root.geometry('220x130')
root.mainloop()

