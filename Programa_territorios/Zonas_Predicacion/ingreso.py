from customtkinter import CTkFrame, CTkLabel
from widgets import CasillaBoton

zona_1 = list(range(1, 28))
zona_2 = list(range(28, 42))
zona_3 = list(range(42, 61))


class PestanaIngreso:
    def __init__(self, parent, gestor):
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure((0, 1, 2), weight=1, uniform="col")

        self.crear_zona(parent, 0, "Zona 1", zona_1, gestor)
        self.crear_zona(parent, 1, "Zona 2", zona_2, gestor)
        self.crear_zona(parent, 2, "Zona 3", zona_3, gestor)

    def crear_zona(self, parent, columna, titulo, numeros, gestor):
        zona = CTkFrame(parent, corner_radius=10)
        zona.grid(row=0, column=columna, padx=10, pady=10, sticky="nsew")

        CTkLabel(zona, text=titulo, font=("Arial", 16)).pack(pady=10)
        contenedor = CTkFrame(zona, fg_color="transparent")
        contenedor.pack(expand=True, fill="both", padx=10, pady=10)

        filas = (len(numeros) // 5) + 1
        zona_num = titulo.split()[1]

        for i, num in enumerate(numeros):
            fila = i // 5
            col = i % 5
            boton = CasillaBoton(contenedor, zona_num, str(num), gestor)
            boton.grid(row=fila, column=col, padx=5, pady=5)
