from customtkinter import CTkButton


class CasillaBoton(CTkButton):
    def __init__(self, master, zona, numero, gestor):
        super().__init__(master, text=numero, width=40, height=40,
                         corner_radius=5, fg_color="#eeeeee", text_color="#333333",
                         hover_color="#dddddd", command=self.toggle)
        self.numero = numero
        self.zona = zona
        self.gestor = gestor
        self.seleccionado = False

    def toggle(self):
        self.gestor.seleccionar(self)

    def seleccionar(self):
        self.seleccionado = True
        self.configure(fg_color="#448aff", text_color="white")

    def deseleccionar(self):
        self.seleccionado = False
        self.configure(fg_color="#eeeeee", text_color="#333333")
