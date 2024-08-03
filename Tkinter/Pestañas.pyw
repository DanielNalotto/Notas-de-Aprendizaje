import tkinter
from tkinter import ttk

master = tkinter.Tk()


notebook = ttk.Notebook(master)
notebook.pack(fill='both', expand='yes')
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='Uno')
notebook.add(frame2, text='Dos')


master.geometry('200x200')
master.mainloop()
