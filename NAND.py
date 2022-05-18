from Pieza import *

class NAND(Pieza):
    def __init__(self, entrada1, entrada2):
        super().__init__(entrada1, entrada2)
        # self.image = load_image("NAND.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1 and self.entrada2 == 1:
            self.salida = 0
        else:
            self.salida = 1

if __name__ == '__main__': #COMPROVAR QUE FUNCIONA BIEN
    n = NAND(0,0)
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)