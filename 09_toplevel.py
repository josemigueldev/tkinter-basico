import tkinter

ventana = tkinter.Tk()
ventana.title("Ventana Principal")
ventana.geometry("250x250")


def enviar_nombre(nombre):
    ventana_nueva = tkinter.Toplevel()
    ventana_nueva.title("Ventana Secundaria")
    ventana_nueva.geometry("250x150")

    etiqueta = tkinter.Label(ventana_nueva, text=f"Nombre: {nombre}")
    etiqueta.grid(row=0, padx=10, pady=10)

    boton_cerrar = tkinter.Button(
        ventana_nueva,
        text="Cerrar Ventana",
        command=ventana_nueva.destroy
    ).grid(row=1, padx=10)


entrada = tkinter.Entry(ventana)
entrada.grid(row=0, pady=10, padx=10, ipady=5, ipadx=30)

boton = tkinter.Button(ventana, text="Enviar", command=lambda:enviar_nombre(entrada.get()))
boton.grid(row=1)

ventana.mainloop()
