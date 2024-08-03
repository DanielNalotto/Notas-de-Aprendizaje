from tkinter import*
raiz=Tk()
raiz.title("Primer Ventana")
raiz.resizable(False,False)
raiz.iconbitmap("io.ico")
raiz.config(bg="sky blue")

#Crea la variable del Frame "nombre_del_Frame=Frame()"
miFrame=Frame()

#Empaqueta el frame
miFrame.pack()

#Le da color al frame (bg= background) el color tiene que estar en inglés
miFrame.config(bg="grey")

#Tamaño del frame
miFrame.config(width="650", height="350")

raiz.mainloop()
