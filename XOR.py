from Pieza import *

class XOR(Pieza):
    def __init__(self):
        super(XOR, self).__init__()
        #self.image = load_image("XOR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 != self.entrada2:
            self.salida = 1
        else:
            self.salida = 0


if __name__ == '__main__':
    n = XOR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)