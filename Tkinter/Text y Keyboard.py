from tkinter import*
import pyautogui
from tkinter import messagebox
import keyboard

root = Tk()
root.geometry('210x248')

def ev():
    a = t.get(1.0, END)
    if a == '\n':
        messagebox.showerror('Prueba','Escribí algo putis, sino no tiene gracia ¬.¬')
    else:
        pyautogui.moveTo(460,745)
        pyautogui.click(button='left')
        keyboard.write(a)
    

t = Text(root, wrap=WORD)
t.place(x=5, y=5, width=200, height=200)

b = Button(root, text='Aceptar', command=ev)
b.place(x=60, y=210, height=30, width=90)

root.mainloop()
