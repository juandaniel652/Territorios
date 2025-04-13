from tkinter import ttk
from customtkinter import CTkFrame, CTkButton
import sqlite3
import pandas as pd
from tkinter import filedialog

class PestanaRegistros:
    def __init__(self, parent):
        self.frame = CTkFrame(parent)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        # 🧪 Estilo moderno
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="#2b2b2b",  # fondo filas
                        foreground="white",    # texto
                        rowheight=30,
                        fieldbackground="#2b2b2b",
                        font=("Segoe UI", 11))

        style.configure("Treeview.Heading",
                        background="#1f1f1f",  # fondo encabezado
                        foreground="white",
                        font=("Segoe UI", 12, "bold"))

        style.map("Treeview",
                  background=[("selected", "#3a7ff6")],
                  foreground=[("selected", "white")])

        # Tabla
        self.tree = ttk.Treeview(self.frame, columns=("zona", "numero", "conductor", "fecha", "cuadras", "asignacion", "completado"), show="headings")
        self.tree.pack(fill="both", expand=True)

        # Encabezados
        self.tree.heading("zona", text="Zona")
        self.tree.heading("numero", text="Número")
        self.tree.heading("conductor", text="Conductor")
        self.tree.heading("fecha", text="Fecha Registro")
        self.tree.heading("cuadras", text="Cuadras")
        self.tree.heading("asignacion", text="Fecha Asignación")
        self.tree.heading("completado", text="Fecha Completado")

        # Ajustar el ancho según el contenido del título
        self.tree.column("zona", width=60, anchor="center")
        self.tree.column("numero", width=80, anchor="center")
        self.tree.column("conductor", width=150, anchor="center")
        self.tree.column("fecha", width=120, anchor="center")
        self.tree.column("cuadras", width=100, anchor="center")
        self.tree.column("asignacion", width=140, anchor="center")
        self.tree.column("completado", width=150, anchor="center")

        CTkButton(self.frame, text="Actualizar registros", command=self.cargar_datos).pack(pady=10)
        CTkButton(self.frame, text="Exportar a Excel", command=self.exportar_excel).pack(pady=5)


        self.cargar_datos()

    def cargar_datos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect("planillas.db")
        cursor = conn.cursor()
        cursor.execute("""
        SELECT zona, numero, conductor, fecha, cuadras, fecha_asignacion, fecha_completado
        FROM planillas
        ORDER BY fecha_completado ASC
        """)
        filas = cursor.fetchall()
        conn.close()

        for fila in filas:
            self.tree.insert("", "end", values=fila)


    def exportar_excel(self):
        conn = sqlite3.connect("planillas.db")
        df = pd.read_sql_query("SELECT * FROM planillas", conn)
        conn.close()

        archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

        if archivo:
            df.to_excel(archivo, index=False)
