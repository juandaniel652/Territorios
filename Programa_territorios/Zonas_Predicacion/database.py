import sqlite3

def inicializar_db():
    conn = sqlite3.connect("planillas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS planillas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zona TEXT NOT NULL,
            numero TEXT NOT NULL,
            conductor TEXT,
            fecha TEXT,
            cuadras TEXT,
            fecha_asignacion TEXT,
            fecha_completado TEXT
        )
    """)
    conn.commit()
    conn.close()


def guardar_planilla(zona, numero, conductor, fecha, cuadras, fecha_asignacion, fecha_completado):
    conn = sqlite3.connect("planillas.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO planillas (zona, numero, conductor, fecha, cuadras, fecha_asignacion, fecha_completado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (zona, numero, conductor, fecha, cuadras, fecha_asignacion, fecha_completado))
    conn.commit()
    conn.close()
