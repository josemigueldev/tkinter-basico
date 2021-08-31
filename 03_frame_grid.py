import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x600")  # anchoxalto

marco1 = tkinter.Frame()
marco1.config(width=200, height=200, bg="red")
marco1.grid(row=0, column=1)

marco2 = tkinter.Frame()
marco2.config(width=200, height=200, bg="green")
marco2.grid(row=0, column=0)

marco3 = tkinter.Frame()
marco3.config(width=200, height=200, bg="blue")
marco3.grid(row=1, column=0)

marco4 = tkinter.Frame()
marco4.config(width=200, height=200, bg="purple")
marco4.grid(row=1, column=1)

marco5 = tkinter.Frame()
marco5.config(width=200, height=200, bg="orange")
marco5.grid(row=2, column=0)

marco6 = tkinter.Frame()
marco6.config(width=200, height=200, bg="brown")
marco6.grid(row=2, column=1)

boton1 = tkinter.Button(ventana, text="Boton 1", bg="#22577A", fg="white", padx=50, pady=10)
boton1.grid(row=1, column=0)

boton2 = tkinter.Button(ventana, text="Boton 2", padx=50, pady=10, state=tkinter.DISABLED)
boton2.grid(row=1, column=1)

ventana.mainloop()
