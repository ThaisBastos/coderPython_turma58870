#teste_retangulo.py

from geometria import Retangulo

def main():
    retangulo = Retangulo(2, 4)

    print(f"Area do retangulo: {retangulo.area()}")

    print(f"Perimetro do retangulo: {retangulo.perimetro()}")

if __name__ == "__main__":
    main()
