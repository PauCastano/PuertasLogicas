

class Pieza:
    # Definicion del comportamiento de las piezas en general
    def __init__(self, entrada1 = 0, entrada2 = 0):
        self.entrada1 = entrada1
        self.entrada2 = entrada2

    def mov(self):
        self.speed = [4, 4]
