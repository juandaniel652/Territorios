from customtkinter import CTkLabel, CTkEntry, CTkFrame, CTkButton, CTkToplevel
from datetime import date
from database import guardar_planilla


class PestanaPlanillas:
    def __init__(self, parent):
        CTkLabel(parent, text="Formulario de Registro", font=("Arial", 20)).pack(pady=10)

        self.parent = parent
        self.formulario = CTkFrame(parent, corner_radius=10)
        self.formulario.pack(padx=20, pady=10, fill="x")

        self.entrada_zona = self.crear_entrada("Zona:", True)
        self.entrada_numero = self.crear_entrada("Número:", True)
        self.entrada_conductor = self.crear_entrada("Conductor:")
        self.entrada_fecha = self.crear_entrada("Fecha actual:", False, valor=date.today().strftime("%Y-%m-%d"))
        self.entrada_cuadras = self.crear_entrada("Cuadras completadas:")

        self.entrada_asignacion = self.crear_entrada("Fecha de asignación:")
        self.entrada_completado = self.crear_entrada("Fecha de completado:")

        self.boton_guardar = CTkButton(parent, text="Guardar", command=self.guardar)
        self.boton_guardar.pack(pady=10)

    def crear_entrada(self, label, deshabilitado=False, valor=""):
        frame = CTkFrame(self.formulario, fg_color="transparent")
        frame.pack(pady=5, fill="x")

        CTkLabel(frame, text=label, width=150, anchor="w").pack(side="left", padx=5)
        entrada = CTkEntry(frame)
        entrada.pack(side="left", fill="x", expand=True, padx=5)
        entrada.insert(0, valor)

        if deshabilitado:
            entrada.configure(state="disabled")
        return entrada

    def cargar_datos(self, zona, numero):
        self.entrada_zona.configure(state="normal")
        self.entrada_numero.configure(state="normal")

        self.entrada_zona.delete(0, "end")
        self.entrada_numero.delete(0, "end")

        self.entrada_zona.insert(0, zona)
        self.entrada_numero.insert(0, numero)

        self.entrada_zona.configure(state="disabled")
        self.entrada_numero.configure(state="disabled")

        self.entrada_conductor.delete(0, "end")
        self.entrada_cuadras.delete(0, "end")
        self.entrada_fecha.delete(0, "end")
        self.entrada_fecha.insert(0, date.today().strftime("%d - %m - %Y"))
        self.entrada_asignacion.delete(0, "end")
        self.entrada_completado.delete(0, "end")

    def guardar(self):
        zona = self.entrada_zona.get()
        numero = self.entrada_numero.get()
        conductor = self.entrada_conductor.get()
        fecha = self.entrada_fecha.get()
        cuadras = self.entrada_cuadras.get()
        fecha_asignacion = self.entrada_asignacion.get()
        fecha_completado = self.entrada_completado.get()

        guardar_planilla(zona, numero, conductor, fecha, cuadras, fecha_asignacion, fecha_completado)
        self.mostrar_alerta("¡Datos guardados exitosamente!")
        print("✔ Datos guardados con éxito.")

    def mostrar_alerta(self, mensaje):

        ventana = CTkToplevel(self.parent)
        ventana.title("Confirmación")
        ventana.geometry("300x150")
        ventana.resizable(False, False)
        ventana.attributes("-topmost", True)  # Siempre al frente

        CTkLabel(ventana, text="✅", font=("Arial", 40), text_color="green").pack(pady=(10, 0))
        CTkLabel(ventana, text=mensaje, font=("Segoe UI", 14)).pack(pady=(5, 10))

        CTkButton(ventana, text="OK", command=ventana.destroy).pack()