from Pieza import *

class XOR(Pieza):
    def __init__(self, entrada1=0, entrada2=0):
        super().__init__(entrada1, entrada2)
        #self.image = load_image("XOR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = self.entrada1^self.entrada2


if __name__ == '__main__':
    n = XOR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)