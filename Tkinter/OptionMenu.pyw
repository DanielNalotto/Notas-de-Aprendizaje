from tkinter import *

# Top level window 
window = Tk()

window.title("Studyfied.com")
window.geometry('350x200')

# Option menu variable
optionVar = StringVar()
optionVar.set("Red")

# Create a option menuy
option_list=["Red", "Blue", "White", "Black"]
option = OptionMenu(window, optionVar, *option_list)
option.pack()

# Create button with command
def show():
    Label(window, textvariable=str(optionVar)).pack()

btnShow = Button(window, text="Show", command=show)
btnShow.pack()

window.mainloop()
