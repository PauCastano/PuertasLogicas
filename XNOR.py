from Pieza import *

class XNOR(Pieza):
    def __init__(self):
        super(XNOR, self).__init__()
        self.image = load_image("XNOR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == self.entrada2:
            salida = 1
        else:
            salida = 0
        return salida