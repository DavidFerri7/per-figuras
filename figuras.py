import math

class Figura():
    def __init__(self):
        print("Estab figura no tiene area.")

    def get_area(self):
        pass

    def get_perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self,lado):

        self.lado = lado

    def get_area(self):
        return self.lado * self.lado

    def get_perimetro(self):
        return self.lado*4


class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio

    def get_area(self):
        return math.pi*((self.radio)**2)

    def get_perimetro(self):
        return (self.radio)*2*math.pi


class Rectangulo(Figura):
    def __init__(self,L,l):
        self.L = L
        self.l = l

    def get_area(self):
        return self.L*self.l

    def get_perimetro(self):
        return self.L*2 + self.l*2



cuadrado=Cuadrado(7)
area_cuadrado = cuadrado.get_area()
peri_cuadrado = cuadrado.get_perimetro()
print("El area del cuadrado es:",area_cuadrado)
print("Y su perimetro:",peri_cuadrado)

circulo = Circulo(3)
t = circulo.get_area()
g = circulo.get_perimetro()
print("El area del circulo es:", t)
print("Y su perimetro:",g)

rectangulo = Rectangulo(4,5)
u = rectangulo.get_area()
v = rectangulo.get_perimetro()
print("El area del rectangulo es:", u)
print("y su perimetro:",v)
