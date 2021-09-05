from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
indice = 0

# Funciones
def click_boton(valor):
    # con global accedemos a la variable global indice que declaramos antes y
    # asi poder actualizar su valor desde la funcion click_boton
    global indice
    pantalla.insert(indice, valor)
    indice += 1

def limpiar_pantalla():
    # borramos pantalla
    pantalla.delete(0, END)  # END <=> tkinter.END
    indice = 0

def operacion():
    ecuacion = pantalla.get()
    resultado = eval(ecuacion)
    pantalla.delete(0, END)  # borramos pantalla
    pantalla.insert(0, resultado)  # insertamos el resultado
    indice = 0

# Pantalla
pantalla = Entry(ventana, font=("Arial", 15))
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5), ipady=10, sticky="WE")
# sticky: estiramos a los lados y con ipady damos altura en el eje Y

# Botones
boton1 = Button(ventana, text="1", width=5, height=2, command=lambda:click_boton(1))
boton2 = Button(ventana, text="2", width=5, height=2, command=lambda:click_boton(2))
boton3 = Button(ventana, text="3", width=5, height=2, command=lambda:click_boton(3))
boton4 = Button(ventana, text="4", width=5, height=2, command=lambda:click_boton(4))
boton5 = Button(ventana, text="5", width=5, height=2, command=lambda:click_boton(5))
boton6 = Button(ventana, text="6", width=5, height=2, command=lambda:click_boton(6))
boton7 = Button(ventana, text="7", width=5, height=2, command=lambda:click_boton(7))
boton8 = Button(ventana, text="8", width=5, height=2, command=lambda:click_boton(8))
boton9 = Button(ventana, text="9", width=5, height=2, command=lambda:click_boton(9))
boton0 = Button(ventana, text="0", width=5, height=2, command=lambda:click_boton(0))

borrar = Button(ventana, text="AC", width=5, height=2, command=limpiar_pantalla)
parentesis_1 = Button(ventana, text="(", width=5, height=2, command=lambda:click_boton("("))
parentesis_2 = Button(ventana, text=")", width=5, height=2, command=lambda:click_boton(")"))
punto = Button(ventana, text=".", width=5, height=2, command=lambda:click_boton("."))

division = Button(ventana, text="÷", width=5, height=2, command=lambda:click_boton("/"))
multiplicacion = Button(ventana, text="×", width=5, height=2, command=lambda:click_boton("*"))
suma = Button(ventana, text="+", width=5, height=2, command=lambda:click_boton("+"))
resta = Button(ventana, text="-", width=5, height=2, command=lambda:click_boton("-"))
igual = Button(ventana, text="=", width=5, height=2, command=operacion)

# Grid
borrar.grid(row=1, column=0, padx=(10, 5), pady=5)
parentesis_1.grid(row=1, column=1, padx=5, pady=5)
parentesis_2.grid(row=1, column=2, padx=5, pady=5)
division.grid(row=1, column=3, padx=(5, 10), pady=5)

boton7.grid(row=2, column=0, padx=(10, 5), pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
multiplicacion.grid(row=2, column=3, padx=(5, 10), pady=5)

boton4.grid(row=3, column=0, padx=(10, 5), pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
suma.grid(row=3, column=3, padx=(5, 10), pady=5)

boton1.grid(row=4, column=0, padx=(10, 5), pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
resta.grid(row=4, column=3, padx=(5, 10), pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=(10, 5), pady=(5, 10), sticky="WE")
punto.grid(row=5, column=2, padx=5, pady=(5, 10))
igual.grid(row=5, column=3, padx=(5, 10), pady=(5, 10))

ventana.mainloop()
