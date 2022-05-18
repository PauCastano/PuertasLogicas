from Pieza import *

class OR(Pieza):

    def __init__(self, entrada1, entrada2):
        super().__init__(entrada1, entrada2)
        #self.image = load_image("OR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1:
            self.salida = 1
        elif self.entrada2 == 1:
           self.salida = 1
        else:
            self.salida = 0

if __name__ == '__main__':
    n = OR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)