from tkinter import*
import tkinter as tk


class pj:
    def __init__(self):
        self.nombre=''
        self.io=''
        self.habilidad=''
    
    def datos(self):
        print("Nombre: " + self.nombre + "\nIo: " + self.io + "\nHabilidad: " + self.habilidad)
        
yusuke=pj()
yusuke.nombre="Yusuke"
yusuke.io="Negro"
yusuke.habilidad="Cortar"

shio=pj()
shio.nombre="Shio"
shio.io="Amarillo"
shio.habilidad="Curar"

haru=pj()
haru.nombre="Haru"
haru.io="Rojo"
haru.habilidad="Rigidez"

def escoger_personaje():

    print("""Personajes\n
    1_Yusuke
    2_Haru
    3_Shio\n""")

    op=input("Escoge tu personaje: ")

    if op == 1:
        yusuke.datos()
    elif op == 2:
        haru.datos()
    elif op == 3:
        shio.datos()
x=input("numero: ")
def ja():
    global x
    if x == 1:
        yusuke.datos()
    elif x==2:
        haru.datos()
ja()
#escoger_personaje()