from Pieza import *

class AND(Pieza):

    def __init__(self, entrada1=0, entrada2=0):
        super().__init__(entrada1, entrada2)
        #self.image = load_image("AND.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1 and self.entrada2 == 1:
            self.salida = 1
        else:
            self.salida = 0
if __name__ == '__main__':
    n = AND()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)