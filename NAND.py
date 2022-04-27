from Pieza import *

class NAND(Pieza):
    def __init__(self):
        super(NAND, self).__init__()
        self.image = load_image("NAND.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1 and self.entrada2 == 1:
            salida = 0
        else:
            salida = 1
        return salida