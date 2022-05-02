class NIVEL:
    # Definicion del comportamiento
    def __init__(self, resultado_final):
        self.resultado_final = resultado_final
    #si la salida es 1 quiere decir que el nivel esta superado
    def comp (self):
        if self.resultado_final == 1:
            snivel = 1
        else:
            snivel = 0
        return snivel
