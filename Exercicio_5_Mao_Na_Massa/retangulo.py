class Retangulo:
    def __init__(self, base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

retangulo = Retangulo(2, 4)

print(f"Area do retangulo: {retangulo.area()}")

print(f"Perimetro do retangulo: {retangulo.perimetro()}")