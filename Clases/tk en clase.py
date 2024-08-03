from tkinter import*
import tkinter as tk


class UI(tk.Frame):
    """Docstring.""" #ESTO SERÍA LA ACLARACIÓN DE LO QUE HACE LA CLASE Y/O DEFINICIÓN

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        #ACÁ VAN LOS WIDGETS
        
        Entry(self.parent).pack()
        Label(self.parent, text="Nah mames si funca").pack()
        
        #CÓMO SE VIO RECIÉN XD
        
        self.parent.title("Titulo")

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("800x600")
    APP = UI(parent=ROOT)
    APP.mainloop()
