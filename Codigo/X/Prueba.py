from tkinter import *
from tkinter import messagebox
import time
import os
import keyboard
from gif import gifmodel
from tkinter import ttk

ws = Tk()
ws.title('Asistente')
ws.geometry('1200x600')
ws.config(bg='#345')

class fram:

    def quitWin(self,info):
        res = messagebox.askyesno('Asistente', '¿Desea activar al asistente?')

        if res == True:
            print("GIF",info)
            g=gifmodel(info)

            def close_win(e):
                ws.destroy()
            ws.bind('<Escape>', lambda e: close_win(e))

        elif res == False:

            #exit()
            pass
        else:
            messagebox.showerror('Error', 'Hubo un problema')
    def __init__(self, info):
        Button(ws, text='Presione para activar al asistente', padx=10, pady=5, command=self.quitWin(info)).pack(pady=50)
        ws.mainloop()

#f=fram('1-1')