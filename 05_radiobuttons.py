import tkinter
"""
Variables de control:
    IntVar()
    DoubleVar()
    StringVar()
    BooleanVar()
"""
ventana = tkinter.Tk()
ventana.geometry("250x250")

x = tkinter.IntVar()
x.set(value=1)  # marcar la opcion uno por defecto

def actualizar_valor(valor):
    # pintamos el valor del radiobutton en un label
    valor_opcion = tkinter.Label(ventana, text=valor).grid(row=4)

titulo = tkinter.Label(ventana, text="Seleccione una respuesta.").grid(row=0)

opcion1 = tkinter.Radiobutton(
    ventana,
    text="Esta es la primera opcion",
    value=1,
    variable=x).grid(row=1)

opcion2 = tkinter.Radiobutton(
    ventana,
    text="Esta es la segunda opcion",
    value=2,
    variable=x).grid(row=2)

boton = tkinter.Button(
    ventana,
    text="Enviar",
    command=lambda:actualizar_valor(x.get())
).grid(row=3)

ventana.mainloop()
