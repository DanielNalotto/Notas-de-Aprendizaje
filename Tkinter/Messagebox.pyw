from tkinter import messagebox
from tkinter import*

root=Tk()

def error():
    messagebox.showerror("Error", "No piola")    

def war():
    messagebox.showwarning("Warning", "Cuidado")

def info():
    messagebox.showinfo("Info", "Piola")

def a1():
    messagebox.askyesno("Pregunta", "Ah, ¿o no que está copado este?")
    
def a2():
    n= messagebox.askokcancel("Pregunta","Acepta si estas de acuerdo en que Dan es genial.")
    while True:
        if n == False:
            m= messagebox.askretrycancel("Respuesta", "Su respuesta es incorrecta.\n¿Quiere reintentarlo?")
            if m == True:
                n= messagebox.askokcancel("Pregunta","Acepta si estas de acuerdo en que Dan es genial.")
            else:
                messagebox.showinfo("Aclaración", "Usted es un envidioso, vuelva a intentarlo.")
                n= messagebox.askokcancel("Pregunta","Acepta si estas de acuerdo en que Dan es genial.")
        else:
            messagebox.showinfo("Aclaración", "Ya todos sabemos que Dan es genial B)")
            break
            

Button(root, text="Error", command=error, width=20).pack()
Button(root, text="Warning", command=war, width=20).pack()
Button(root, text="Info", command=info, width=20).pack()
Button(root, text="Sí o No", command=a1, width=20).pack()
Button(root, text="Ok, Cancel", command=a2, width=20).pack()
