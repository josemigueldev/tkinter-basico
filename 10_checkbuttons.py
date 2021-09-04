import tkinter

ventana = tkinter.Tk()
ventana.title("Ventana Principal")
ventana.geometry("350x300")

control_entero = tkinter.IntVar()
control_cadena = tkinter.StringVar()

def seleccion():
    etiqueta1 = tkinter.Label(ventana, text=control_entero.get())
    etiqueta1.pack()
    etiqueta2 = tkinter.Label(ventana, text=control_cadena.get())
    etiqueta2.pack()

opcion1 = tkinter.Checkbutton(
    ventana,
    text="Opcion 1",
    variable=control_entero,
    onvalue=1,
    offvalue=-1
)
opcion1.deselect()  # para que no tome el valor por defecto de 0
opcion1.pack()

opcion2 = tkinter.Checkbutton(
    ventana,
    text="Opcion 2",
    variable=control_cadena,
    onvalue="Opcion 2 seleccionada",
    offvalue="Opcion 2 NO seleccionada"
)
opcion2.deselect()  # para que no tome el valor por defecto
opcion2.pack()

boton = tkinter.Button(ventana, text="Mostrar seleccion", command=seleccion)
boton.pack()

ventana.mainloop()
