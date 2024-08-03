from tkinter import Tk, Label, Frame
from GUI import *

if __name__ == "__main__":
    root=Tk()
    root.geometry('500x500')
    Label(root).pack()
    f = Frame(root, bg='red')
    f.place(x=20, y=20, width=400, height=300)
    a = coco.Coco_btn(f)
    root.mainloop()