from tkinter import *

root = Tk()

frame1 = Frame (root)
frame1.grid(row=1, column=0, padx=3, pady=3, columnspan=3)

frame2 = Frame (root)
frame2.grid(row=0, column=0, padx=3, pady=3, columnspan=3)

# ------- CONSTANTES -------------

# ------- VARIABLES --------------

FUE = IntVar()
DES = IntVar()

FUE_mod = IntVar()
DES_mod = IntVar()

FUE_ts = IntVar()
DES_ts = IntVar()

#--------------------

name = StringVar()
levl = IntVar()
boni = IntVar()

# ------- DEFINICIONES -----------

def calcular_nivel():
    if levl.get == 1 or levl.get() == 2 or levl.get() == 3 or levl.get() == 4:
        bonif = 2
    elif levl.get == 5 or levl.get() == 6 or levl.get() == 7 or levl.get() == 8:
        bonif = 3
    elif levl.get == 9 or levl.get() == 10 or levl.get() == 11 or levl.get() == 12:
        bonif = 4
    elif levl.get == 13 or levl.get() == 14 or levl.get() == 15 or levl.get() == 16:
        bonif = 5
    elif levl.get == 17 or levl.get() == 18 or levl.get() == 19 or levl.get() == 20:
        bonif = 6

def calcular_stat(stat):
    if stat == 1:
        mod = -5

    elif stat == 2 or stat == 3:
        mod = -4

    elif stat == 4 or stat == 5:
        mod = -3

    elif stat == 6 or stat == 7:
        mod = -2

    elif stat == 8 or stat == 9:
        mod = -1

    elif stat == 10 or stat == 11:
        mod = 0

    elif stat == 12 or stat == 13:
        mod = 1

    elif stat == 14 or stat == 15:
        mod = 2

    elif stat == 16 or stat == 17:
        mod = 3

    elif stat == 18 or stat == 19:
        mod = 4

    elif stat == 20:
        mod = 5

def act():
    calcular_nivel()

    FUE_mod.set(calcular_stat(FUE.get()))
    DES_mod.set(calcular_stat(DES.get()))
    boni.set(bonif)
# --------------------------------

#Nombre
l_nombre = Label (frame2, text='Nombre:')
l_nombre.grid(row=0, column=0, padx=3, pady=3)

e_nombre = Entry (frame2, textvariable=name)
e_nombre.grid(row=0, column=1, padx=3, pady=3)

#Nivel
l_nivel = Label (frame2, text='nivel:')
l_nivel.grid(row=0, column=2, padx=3, pady=3)

e_nivel = Entry (frame2, textvariable=levl, width=3)
e_nivel.grid(row=0, column=3, padx=3, pady=3)

#Bonificador
l_bonificador = Label (frame2, text='Bonificador:')
l_bonificador.grid(row=0, column=4, padx=3, pady=3)

e_bonificador = Entry (frame2, textvariable=boni, width=3, state='readonly')
e_bonificador.grid(row=0, column=5, padx=3, pady=3)


# --------------------------------
#Fuerza
l_FUE = Label (frame1, text='FUE:')
l_FUE.grid(row=0, column=0, padx=3, pady=3)

e_FUE = Entry (frame1, textvariable=FUE, width=3)
e_FUE.grid(row=0, column=1, padx=3, pady=3)

l_FUE_mod = Label (frame1, text='mod')
l_FUE_mod.grid(row=0, column=2, padx=3, pady=3)

e_FUE_mod = Entry (frame1, textvariable = FUE_mod, width=3, state='readonly')
e_FUE_mod.grid(row=0, column=3, padx=3, pady=3)

l_FUE_ts = Label (frame1, text='TS')
l_FUE_ts.grid(row=0, column=4, padx=3, pady=3)

e_FUE_ts = Entry (frame1, textvariable = FUE_ts, width=3, state='readonly')
e_FUE_ts.grid(row=0, column=5, padx=3, pady=3)

#Destreza
l_DES = Label (frame1, text='DES:')
l_DES.grid(row=1, column=0, padx=3, pady=3)

e_DES = Entry (frame1, textvariable=DES, width=3)
e_DES.grid(row=1, column=1, padx=3, pady=3)

l_DES_mod = Label (frame1, text='mod')
l_DES_mod.grid(row=1, column=2, padx=3, pady=3)

e_DES_mod = Entry (frame1, textvariable = DES_mod, width=3, state='readonly')
e_DES_mod.grid(row=1, column=3, padx=3, pady=3)

l_DES_ts = Label (frame1, text='TS')
l_DES_ts.grid(row=1, column=4, padx=3, pady=3)

e_DES_ts = Entry (frame1, textvariable = DES_ts, width=3, state='readonly')
e_DES_ts.grid(row=1, column=5, padx=3, pady=3)

# -----------------------------------

Button (root, text='Actualizar', command=act).grid(row=2, column=1)
# --------------------------------
root.mainloop()
