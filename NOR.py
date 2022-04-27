from Pieza import *

class NOR(Pieza):
    def __init__(self):
        super(NOR, self).__init__()
        self.image = load_image("NOR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if (self.entrada1 == 0) and (self.entrada2 == 0):
            salida = 1
        else:
            salida = 0
        return salida