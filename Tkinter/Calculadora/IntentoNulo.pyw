from tkinter import*

raiz=Tk()

calcu=Frame(raiz)
calcu.pack()

pantalla=Entry(calcu)
pantalla.grid(row=1, column=1, padx=10, pady=10)
pantalla.config(background="aquamarine", fg="medium orchid", justify="right")


raiz.mainloop()
