from tkinter import Frame, Button

class Coco_btn(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

    def GUI(self):
        Button(self.parent, text="Pennaut", command=lambda:self.return_text()).pack()

    def return_text(self):
        return "Up your but with a cocconout"


    
