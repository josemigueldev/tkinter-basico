import tkinter

ventana = tkinter.Tk()
ventana.geometry("300x160")

colores = [
    ["Color Rojo", "rojo"],
    ["Color Verde", "verde"],
    ["Color Azul", "azul"],
]

color = tkinter.StringVar()
color.set("rojo")  # opcion por defecto seleccionada

def actualizar_valor():
    valor_opcion.config(text=color.get())

titulo = tkinter.Label(ventana, text="Seleccione una respuesta.")
titulo.pack()

for opcion, valor in colores:
    tkinter.Radiobutton(ventana, text=opcion, value=valor, variable=color).pack(anchor="w")

boton = tkinter.Button(
    ventana,
    text="Enviar",
    command=actualizar_valor
).pack()

valor_opcion = tkinter.Label(ventana, text=color.get())
valor_opcion.pack()

ventana.mainloop()
