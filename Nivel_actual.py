from NIVEL import *
class Nivel_actual:

    # Iniciamos el primer nivel
    def __init__(self, nivel_actual = 1):
        self.nivel_actual = nivel_actual

    #Función para indicar cual es el nivel actual según la salida del nivel
    def nivel_actual(self, nivel_actual):
        if self.comp == 1:
            nivel_actual += 1
        else:
            nivel_actual = nivel_actual
        return nivel_actual