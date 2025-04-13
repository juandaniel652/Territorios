from customtkinter import CTk, CTkTabview
from gestor import GestorSeleccion
from ingreso import PestanaIngreso
from planilla import PestanaPlanillas
from registros import PestanaRegistros
from database import inicializar_db


class VentanaConPestanas:
    def __init__(self):
        self.root = CTk()
        self.root.title("Zonas de Predicación")
        self.root.geometry("900x500")

        self.pestanas = CTkTabview(self.root, width=860, height=450)
        self.pestanas.pack(padx=20, pady=20)

        self.pestanas.add("Ingreso")
        self.pestanas.add("Planillas")
        self.pestanas.add("Registros")

        self.gestor = GestorSeleccion(self)
        self.planilla = PestanaPlanillas(self.pestanas.tab("Planillas"))
        PestanaIngreso(self.pestanas.tab("Ingreso"), self.gestor)
        self.registros = PestanaRegistros(self.pestanas.tab("Registros"))

    def ir_a_planilla(self, zona, numero):
        self.pestanas.set("Planillas")
        self.planilla.cargar_datos(zona, numero)

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    inicializar_db()
    app = VentanaConPestanas()
    app.iniciar()