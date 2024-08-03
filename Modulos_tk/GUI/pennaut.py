from tkinter import Frame, Button

class Pennaut_btn(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

    def GUI(self):
        Button(self.parent, text="Pennaut", command=self.return_text).pack()

    def return_text(self):
        return "It's Pennaut butter jelly time!"