import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x500")  # tamaño de ventana

etiqueta = tkinter.Label(ventana, text="Hola Mundo", bg="#E63E6D", fg="white", height=2, font=("Arial", 14, "italic", "bold"))
# side -> [top, bottom, left, right]
# fill="x" se expande en el eje x (x, y, both -> xy)
# expand=True, se expande segun el valor de fill
etiqueta.pack(side="top", fill="x", expand=False)  # incrusta el label en la ventana

caja_texto = tkinter.Entry(ventana)
caja_texto.pack()  # incrusta la caja de texto en la ventana
caja_texto.focus()  # empieza con el foco en la caja de texto

def saludar(nombre):
    etiqueta_saludar["text"] = f"Hola, {nombre.capitalize()}!"

boton1 = tkinter.Button(ventana, command=lambda:saludar(caja_texto.get()), text="Saludar", width=30, height=2, padx=5, pady=2)
boton1.pack()

etiqueta_saludar = tkinter.Label(ventana)
etiqueta_saludar.pack()

ventana.mainloop()  # la ventana se mantiene abierta
