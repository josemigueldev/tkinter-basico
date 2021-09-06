import tkinter
from tkinter import ttk

def obtener_datos():
    item = arbol.item(arbol.selection())
    print(f"{item['text']}: {item['values'][0]}")

ventana = tkinter.Tk()

arbol = ttk.Treeview(ventana, columns=("#1", "#2", "#3"))
arbol.heading("#0", text="Id")
arbol.heading("#1", text="Nombre")
arbol.heading("#2", text="Email")
arbol.heading("#3", text="Pais")
# insertar dos valores
arbol.insert("", tkinter.END, text="1", values=("Miguel", "miguel21@gmail.com", "Perú"))
arbol.insert("", tkinter.END, text="2", values=("jose", "jose27@gmail.com", "México"))
# modificar tamaños de columnas
arbol.column("#0", width=50)
arbol.column("#1", width=150)
arbol.column("#2", width=200)
arbol.column("#3", width=100)
arbol.pack()

# Obtener datos del item seleccionado
boton = tkinter.Button(ventana, text="Obtener", command=obtener_datos)
boton.pack()

ventana.mainloop()
