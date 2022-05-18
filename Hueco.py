import random
from PuertasL import *

class Hueco:
    def __init__(self, a=random.randint(0, 1), b=random.randint(0, 1)):
        self.a = a
        self.b = b
        self.salida = None

if __name__ == '__main__':
    n = Hueco()
    print(n.a)
    print(n.b)
    print(n.salida)