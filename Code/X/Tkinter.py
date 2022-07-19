from tkinter import *
import os
root = Tk()
def Nivel1():
    os.startfile(r"C:\Juegos\Mario.bat")

myButton = Button(root, text="Cliqueame", command=Nivel1)
myButton.pack()
root.mainloop()

