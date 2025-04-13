class GestorSeleccion:
    def __init__(self, app):
        self.app = app
        self.casilla_seleccionada = None

    def seleccionar(self, casilla):
        if self.casilla_seleccionada is casilla:
            casilla.deseleccionar()
            self.casilla_seleccionada = None
        else:
            if self.casilla_seleccionada:
                self.casilla_seleccionada.deseleccionar()
            casilla.seleccionar()
            self.casilla_seleccionada = casilla
            self.app.ir_a_planilla(casilla.zona, casilla.numero)
