# Crie um programa que defina duas classes círculo e quadrado, a
# classe círculo precisa ter como atributos raio e área, essa mesma
# classe precisa ter um construtor e um método para cálculo da área,
# dada por 3.141*raio*raio. A classe quadrado precisa ter os
# atributos lado e área, um construtor e um destrutor, assim como
# um método para o cálculo da área, dada por lado*lado.

class Circulo:
    def __init__(self,raio):
        self.raio = raio
        self.area = 0.0
        
    def calcular_area(self):
        self.area = 3.141 * (self.raio*self.raio)
        return self.area
    
class Quadrado:
    def __init__(self,lado):
        self.lado = lado
        self.area = 0.0
        
    def calcular_area(self):
        self.area = self.lado*self.lado
        return self.area
    
    def __del__(self):
        print("quadrado destruido!")
        
circulo = Circulo(2)
circulo.calcular_area()
print(f"a area do circulo é:{circulo.area} ")
quadrado = Quadrado(3)
quadrado.calcular_area()
print("a area do quadrado:",quadrado.area)
