from Pieza import *

class OR(Pieza):

    def __init__(self):
        super(OR, self).__init__()
        self.image = load_image("OR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1:
            salida = 1
        elif self.entrada2 == 1:
           salida = 1
        else:
            salida = 0
        return salida
