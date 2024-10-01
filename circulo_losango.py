# Crie um programa que defina duas classes círculo e losango, a
# classe círculo precisa ter como atributos raio e área, essa
# mesma classe precisa ter um construtor e um método para
# cálculo da área, dada por 3.141*raio*raio. A classe losango
# precisa ter os atributos altura, largura e área, um construtor e
# um destrutor, assim como um método para o cálculo da área,
# dada por altura*largura.

class Circulo:
    
    def __init__(self, raio):
        self.raio = raio
        self.area = 0
        
    def calcular_area(self):
        self.area = 3.141 * (self.raio * self.raio)
        return self.area
    
class Losango:
    
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
        self.area = 0
        
    def calcular_area(self):
        self.area  = (self.altura * self.largura)
        return self.area
        
    def __del__(self):
        print("losango destruido")
        
circulo = Circulo(9)
print("A área do circulo é: ", circulo.calcular_area)

losango = Losango(6,9)
print(f"A área do losango com altura {losango.calcular_area} ")


