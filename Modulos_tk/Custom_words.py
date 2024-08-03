from tkinter import Frame, Label

class Custsom_words(Frame):
    def __init__(self, parent, _text):
        Frame.__init__(self, parent)
        self.parent = parent
        self._text = _text

    def GUI(self):
        Label(self.parent, text=self._text).pack()