import sqlite3
from tkinter import *
import tkinter as tk

class Base_de_Datos():
    #Intenta crear la conexion y el cursor, sino, sigue de largo
    try:
        myConection=sqlite3.connect()
        myCursor=myConection.cursor()
    except:
        pass

    #Intenta crear la tabla dentro de la BBDD, sino, sigue de largo
    try:
        myCursor.execute(""""create table DATOS (NOMBRE varchar(50))""")
        myCursor.commit()
    except:
        print("Error 1")

    #Intenta ingresar datos a la tabla, sino, sigue de largo
    try:
        myCursor.execute(""""insert into DATOS values('Hola mundo')""")
        myCursor.commit()
    except:
        print("Error 2")

    #Intenta mostrar los datos de la tabla, sino, sigue de largo
    try:
        myCursor.execute("Select * from DATOS")
        l= myCursor.fetchall()
        for i in l:
            texto=i[0]
            print(i[0])
    except:
        pass





class Formulario(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        e = Entry (self.parent, textvariable=texto)
        e.place(x=75, y=70, width=150, height=20)

        b_guardar = Button(self.parent, text='Guardar')
        b_guardar.place(x=110, y=130, width=80, height=30)

        b_mostrar = Button(self.parent, text='Mostrar', command=lambda:Planilla(self.parent))
        b_mostrar.place(x=110, y=180, width=80, height=30)

class Planilla(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        f=Frame(self.parent)
        f.place(x=0, y=0, width=300, height=300)

        l = Label(f, text=texto.get())
        l.place(x=50, y=50)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.resizable(False, False)

    texto=StringVar()

    app=Formulario(parent=root)
    app.mainloop()