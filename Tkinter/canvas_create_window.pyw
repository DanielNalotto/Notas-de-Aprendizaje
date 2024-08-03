from tkinter import*

root=Tk()

#La opción create_window funciona como marco, no se vé (por lo menos no que
#yo me haya enterado por ahroa :v


#Creas la variable del canvas
canvas=Canvas(root)
canvas.pack()

#Creas un frame que va a ir dentro de la ventana creada
interior = Frame(canvas, bg="red", width=500, height=300)

#Creas la variable del canvas.create_window
#Entre los parentesis van (posición, **opciones)
interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

root.config(bg="black")

root.mainloop()
