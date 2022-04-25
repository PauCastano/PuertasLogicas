class PuertaLogica:

    def __init__(self, entrada1 = 0, entrada2 = 0):

        self.entrada1 = entrada1
        self.entrada2 = entrada2

    def AND(self):
        if self.entrada1 == 1 and self.entrada2 == 1:
            salida = 1
        else:
            salida = 0
        return salida

    def OR(self):
        if self.entrada1 == 1:
            salida = 1
        elif self.entrada2 == 1:
            salida = 1
        else:
            salida = 0
        return salida

    def XOR(self):
        if self.entrada1 != self.entrada2:
            salida = 1
        else:
            salida = 0
        return salida

    def NAND(self):
        if self.entrada1 == 1 and self.entrada2 == 1:
            salida = 0
        else:
            salida = 1
        return salida

    def NOR(self):
        if (self.entrada1 == 0) and (self.entrada2 == 0):
            salida = 1
        else:
            salida = 0
        return salida

    def XNOR(self):
        if self.entrada1 == self.entrada2:
            salida = 1
        else:
            salida = 0
        return salida
