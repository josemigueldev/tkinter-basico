import tkinter

ventana = tkinter.Tk()

# El LabelFrame es como el fieldset de HTML
# pady: padding interno del LabelFrame
buscador = tkinter.LabelFrame(ventana, text="Label Frame", padx=15, pady=15)
# pady: padding externo del grid
buscador.grid(row=0, column=0, padx=30, pady=30)

caja_texto = tkinter.Entry(buscador).pack()
boton = tkinter.Button(buscador, text="Buscar").pack(pady=5)

ventana.mainloop()
