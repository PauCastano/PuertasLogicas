from Pieza import *

class XNOR(Pieza):
    def __init__(self, entrada1=0, entrada2=0):
        super().__init__(entrada1, entrada2)
        #self.image = load_image("XNOR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = int(not (self.entrada1 ^ self.entrada2))


if __name__ == '__main__':
    n = XNOR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)