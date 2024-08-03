from tkinter import*

yus=0

root=Tk()

#Es importante empaquetar de esta manera y no "canvas=Canvas(root).pack()"
#Porque si no queda todo mal y salta error
canvas=Canvas(root)
canvas.pack()

def bot2():
    global yus
    yus +=1
    interior = Frame(canvas, bg="red", width=500, height=300)
    #Si no pones esto, es como si la imagen no se viera
    #Funciona como el empaquetamiento, no se usa el punto pack
    canvas.create_window(0, 0, window=interior, anchor=NW)
    print(yus)

root.config(bg="black")

def bot1():
    global yus
    yus +=1
    i = Frame(canvas, bg="yellow", width=500, height=300)
    canvas.create_window(0, 0, window=i, anchor=NW)
    print(yus)


b1=Button(root, text="Siguiente", command=bot1).pack(side=RIGHT)
b1=Button(root, text="Atrás", command=bot2).pack(side=LEFT)

root.mainloop()
