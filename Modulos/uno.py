from carpeta.dos import*
from tkinter import*

root=Tk()
root.geometry("500x300")
canvas=Canvas(root).pack()
frame=Frame(canvas,bg="red").pack()



b1=Button(frame, text="Yusuke", command=yus).pack()
b2=Button(frame, text="Haru", command=haru).pack()
