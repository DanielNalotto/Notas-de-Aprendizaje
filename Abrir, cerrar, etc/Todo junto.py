from tkinter import*
from def_editor.nuevo import new

root=Tk()
root.title("Editor de Dan")

menubar=Menu(root)
root.config(menu=menubar)

archivo_menu=Menu(menubar, tearoff=0)

menubar.add_cascade(label="Archivo", menu=archivo_menu)

archivo_menu.add_command(label="Nuevo", command=new)
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Salir")

#----------------------------------------------------------------------
t=Text(root)
t.pack(side=LEFT)

barra=Scrollbar(root, command=t.yview)
barra.pack(side=RIGHT, fill=Y)
t.config(yscrollcommand=barra.set)


root.mainloop()
