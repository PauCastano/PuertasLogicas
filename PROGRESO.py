from NIVEL import *
from Nivel_actual import *
class PROGRESO:
    # Guardamos el progreso de los niveles
    def __init__(self, progreso=0):
        self.progreso = progreso

    #Función que indica que el progreso es un número entero y que depende del nivel actual
    def progress(self, progreso):
        # Comportamineto de la Puerta logica
        progreso = self.nivel_actual - 1
        return progreso