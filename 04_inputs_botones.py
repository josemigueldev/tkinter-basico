import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x500")

def click_boton():
    texto = tkinter.Label(ventana, text=f"Se guardo {entrada.get()} correctamente")
    texto.grid(row=2, column=0)

entrada = tkinter.Entry(ventana, width=30, font=("Arial", 15))
entrada.place(height=100)
entrada.grid(row=0, column=0, ipady=10)  # ipady altura para el Entry(padding interno en y)

boton1 = tkinter.Button(ventana, text="Enviar", command=click_boton, padx=50, pady=10)
boton1.grid(row=1, column=0, sticky="W", pady=20) # padding externo en y
# con sticky alineamos el elemento

etiqueta_clave = tkinter.Label(ventana, text="Contraseña:")
etiqueta_clave.grid(row=2, column=0, sticky="W")
entrada_clave = tkinter.Entry(ventana, show="*")
entrada_clave.grid(row=3, column=0, sticky="W")

ventana.mainloop()
