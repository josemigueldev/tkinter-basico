import tkinter
# algunos modulos necesitan ser importados especificamente como este caso
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.geometry("500x450")
ventana.title("Titulo Principal")

def ventana_info():
    messagebox.showinfo(
        title="Ventana de Informacion",
        message="Este es el mensaje de informacion"
    )


def ventana_warning():
    messagebox.showwarning(
        title="Ventana de Advertencia",
        message="Este es el mensaje de advertencia"
    )


def ventana_error():
    messagebox.showerror(
        title="Ventana de Error",
        message="Este es el mensaje de error"
    )


def ventana_pregunta():
    messagebox.askquestion(
        title="Ventana de Pregunta",
        message="Eres mayor de edad?"
    )


def ventana_si_no():
    messagebox.askyesno(
        title="Ventana de Pregunta Yes/No",
        message="Te gusta Python?"
    )


def ventana_si_no_cancelar():
    messagebox.askyesnocancel(
        title="Ventana de Pregunta Yes/No/Cancelar",
        message="Te gusta Python?"
    )


def ventana_reintentar_cancelar():
    messagebox.askretrycancel(
        title="Ventana de Pregunta Reintentar/Cancelar",
        message="Te gusta Python?"
    )


def mayor_edad():
    respuesta = messagebox.askquestion(
        title="Validar Edad",
        message="Eres mayor de edad?"
    )

    if respuesta == "yes":
        # askretrycancel devuelve True o False
        reintentar = messagebox.askretrycancel(
            title="Validar Edad", message="Estas seguro?"
        )
        if reintentar:
            messagebox.showinfo(title="Validar Edad", message="Devolvio True")
        else:
            messagebox.showinfo(title="Validar Edad", message="Devolvio False")

    if respuesta == "no":
        messagebox.showinfo(title="Validar Edad", message="Adios!")


boton1 = tkinter.Button(ventana, text="Info", command=ventana_info)
boton1.pack(pady=10)

boton2 = tkinter.Button(ventana, text="Warning", command=ventana_warning)
boton2.pack(pady=10)

boton3 = tkinter.Button(ventana, text="Error", command=ventana_error)
boton3.pack(pady=10)

boton4 = tkinter.Button(ventana, text="Responder", command=ventana_pregunta)
boton4.pack(pady=10)

boton5 = tkinter.Button(ventana, text="Yes/No", command=ventana_si_no)
boton5.pack(pady=10)

boton6 = tkinter.Button(ventana, text="Yes/No/Cancel", command=ventana_si_no_cancelar)
boton6.pack(pady=10)

boton7 = tkinter.Button(ventana, text="Reintentar/Cancelar", command=ventana_reintentar_cancelar)
boton7.pack(pady=10)

boton8 = tkinter.Button(ventana, text="Mayor Edad", command=mayor_edad)
boton8.pack(pady=10)

ventana.mainloop()
