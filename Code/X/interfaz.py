import tkinter

class Asistente:

    ventana = tkinter.Tk()
    ventana.title("Asistente")
    ventana.geometry("300x100")

    etiqueta= tkinter.Label(ventana, text= "¿Desea activar el asistente?")
    etiqueta.grid(row=0 , column= 1)

    boton1= tkinter.Button(ventana, text= "Sí" , width = 5, height= 0)
    boton2= tkinter.Button(ventana, text= "No" , width = 5, height= 0)

    boton1.grid(row= 2, column= 0)
    boton2.grid(row= 2, column= 2)


    ventana.mainloop()