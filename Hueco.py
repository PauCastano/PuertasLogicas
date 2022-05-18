import random

class Hueco:
    def __init__(self, a=random.randint(0, 1), b=random.randint(0, 1)):
        self.a = a
        self.b = b
        self.salida = None

if __name__ == '__main__':
    n = Hueco()
    print(Hueco().a)
    print(n.b)
    print(n.salida)