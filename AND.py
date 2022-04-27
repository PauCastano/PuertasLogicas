from Pieza import *

class AND(Pieza):

    def __init__(self):
        super(AND, self).__init__()
        self.image = load_image("AND.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1 and self.entrada2 == 1:
            salida = 1
        else:
            salida = 0
        return salida