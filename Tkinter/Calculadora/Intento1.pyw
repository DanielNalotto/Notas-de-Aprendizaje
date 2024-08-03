from tkinter import *

root = Tk()

frame1= Frame (root)
frame1.pack()

frame2 = Frame (root)
frame2.pack()

# --- CONSTANTES -----------------------

altura=2
ancho=5
ancho_pant=28

pad_x =3
pad_y =3

operacion=""
resultado=0

# --- VARIABLES ------------------------

cadena = StringVar()

# --- DEFINICIONES ---------------------

def digito(num):
    
    global operacion

    if operacion !="":

        cadena.set(num)
        operacion=""

    else:
        cadena.set(cadena.get()+ num)

def suma(num):
    
    global operacion
    global resultado

    resultado+=int(num)

    operacion="suma"

    cadena.set(resultado)

def resta(num):

    global operacion
    global resultado

    resultado-=int(num)

    operacion="resta"

    cadena.set(resultado)

def igual():

    global resultado

    cadena.set(resultado+int(cadena.get()))

    resultado=0

def CE():
    global resultado
    global operacion

    resultado=0
    operacion=""
    cadena.set('')

# --- INTERFAZ -------------------------

# PANTALLA

pant = Entry (frame1, state='readonly', width=ancho_pant, justify=RIGHT, textvariable=cadena)
pant.pack(padx=pad_x, pady=pad_y)

# BOTONES

b1 = Button (frame2, width=ancho, height=altura, text='1', command=lambda:digito('1'))
b1.grid(row=0, column=0, padx=pad_x, pady=pad_y)

b2 = Button (frame2, width=ancho, height=altura, text='2', command=lambda:digito('2'))
b2.grid(row=0, column=1, padx=pad_x, pady=pad_y)

b3 = Button (frame2, width=ancho, height=altura, text='3', command=lambda:digito('3'))
b3.grid(row=0, column=2, padx=pad_x, pady=pad_y)

b4 = Button (frame2, width=ancho, height=altura, text='4', command=lambda:digito('4'))
b4.grid(row=1, column=0, padx=pad_x, pady=pad_y)

b5 = Button (frame2, width=ancho, height=altura, text='5', command=lambda:digito('5'))
b5.grid(row=1, column=1, padx=pad_x, pady=pad_y)

b6 = Button (frame2, width=ancho, height=altura, text='6', command=lambda:digito('6'))
b6.grid(row=1, column=2, padx=pad_x, pady=pad_y)

b7 = Button (frame2, width=ancho, height=altura, text='7', command=lambda:digito('7'))
b7.grid(row=2, column=0, padx=pad_x, pady=pad_y)

b8 = Button (frame2, width=ancho, height=altura, text='8', command=lambda:digito('8'))
b8.grid(row=2, column=1, padx=pad_x, pady=pad_y)

b9 = Button (frame2, width=ancho, height=altura, text='9', command=lambda:digito('9'))
b9.grid(row=2, column=2, padx=pad_x, pady=pad_y)

b0 = Button (frame2, width=ancho, height=altura, text='0', command=lambda:digito('0'))
b0.grid(row=3, column=1, padx=pad_x, pady=pad_y)

b_suma = Button (frame2, width=ancho, height=altura, text='+', command=lambda:suma(cadena.get()))
b_suma.grid(row=0, column=3, padx=pad_x, pady=pad_y)

b_resta = Button (frame2, width=ancho, height=altura, text='-', command=lambda:resta(cadena.get()))
b_resta.grid(row=1, column=3, padx=pad_x, pady=pad_y)

b_por = Button (frame2, width=ancho, height=altura, text='x')
b_por.grid(row=2, column=3, padx=pad_x, pady=pad_y)

b_divi = Button (frame2, width=ancho, height=altura, text='/')
b_divi.grid(row=3, column=3, padx=pad_x, pady=pad_y)

b_igual = Button (frame2, width=ancho, height=altura, text='=', command=lambda:igual())
b_igual.grid(row=3, column=2, padx=pad_x, pady=pad_y)

b_CE = Button (frame2, width=ancho, height=altura, text='CE', command=lambda:CE())
b_CE.grid(row=3, column=0, padx=pad_x, pady=pad_y)





root.title('Calculadora')
root.mainloop()
