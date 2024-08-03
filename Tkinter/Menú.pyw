from tkinter import*

raiz=Tk()

menubar=Menu(raiz)
raiz.config(menu=menubar) #Lo asignas a la base, le decis que esta como metido en la raiz o algo así.


# ------ Acá creas la variables del menu ---------
# ------ El "tearoff=0" es para que no te deje ningún "espacio" antes de la primera opción
#Se pone ahí porque sino te jode todoel menu
filemenu=Menu(menubar, tearoff=0)
editmenu=Menu(menubar, tearoff=0)
otromenu=Menu(menubar, tearoff=0)

# ------ Acá haces que se vea la barra ---------
menubar.add_cascade(label="Archivo", menu=filemenu) #Añadis la "cascada" del menu
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Otros", menu=otromenu)

# ------ Acá le metes opciónes a las barras del menu ------
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")

# ------ Ahí le metes separador (ah re obvio) y el comando (ah re obvio también) --------
filemenu.add_separator() 
filemenu.add_command(label="Salir", command=raiz.quit) #No sé de qué sale



raiz.mainloop()
