from tkinter import*

#Hace que laventana aparezca (raiz es el nombre de la variable)
raiz=Tk()

#Nombre de la ventana
raiz.title("Primer Ventana")

#Permite que se pueda modificar o no las dimensiones de la ventana (Altura, ancho)
raiz.resizable(False,False)

#Imagen icono
raiz.iconbitmap("io.ico")

#Fija las dimensiones de la ventana
raiz.geometry("300x200")

#config es para muchas cosas, pero con el bg permite ajustar el color de fondo (Se escribe en ingles)
raiz.config(bg="sky blue")

#Comienza el boocle de la aplicacion, es como un while true
raiz.mainloop()
