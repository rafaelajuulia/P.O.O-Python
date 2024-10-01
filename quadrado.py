# Crie um programa que defina uma classe quadrado, que tenha
# como atributo o lado, receba essa informação do usuário, a classe
# também deve conter um método para calcular e mostrar a área do
# quadrado, dada por lado*lado.

class Quadrado:
    def __init__(self,lado):
        self.lado = lado
        
    def calcular_area(self):
        area = self.lado*self.lado
        return area
    
lado = float(input("informe o valor do lado: "))
quadrado = Quadrado(lado)
print("a area do quadrado é:",quadrado.calcular_area())
        
