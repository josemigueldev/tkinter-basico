import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x500")

logo = tkinter.PhotoImage(file="python_logo.png")
label_logo = tkinter.Label(ventana, image=logo)
label_logo.pack()

ventana.mainloop()
