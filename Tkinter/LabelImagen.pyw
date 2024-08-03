from tkinter import*

dan=Tk()
dan.resizable(False,False)
dan.title("Gremios")

#Para que aparezca la imagen es importante usar los parametros width y height, de lo contrario la imagen no aparecerá.
fondo=Frame(dan, width=630, height=550)
fondo.pack()

#Declaras la variable para la imagen.
foto=PhotoImage(file="naruto.png")

#Usas image para que aparezca
Label(fondo,image=foto).place(x=0, y=0)

fondo.mainloop()
