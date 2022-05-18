from PuertasL import *
from Hueco import *

class Pieza(Hueco):
    # Definicion del comportamiento de las piezas en general
    def __init__(self, entrada1, entrada2):
        super().__init__(entrada1, entrada2)

        self.entrada1 = Hueco.a
        self.entrada2 = Hueco.b
        self.salida = None

if __name__ == '__main__':
    n = Pieza()
    print(Hueco.a)
    print(n.entrada1)
    print(Hueco.b)
    print(n.entrada2)
    print(n.salida)
