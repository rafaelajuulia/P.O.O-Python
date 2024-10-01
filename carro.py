# Crie uma classe simples em Python para representar um
# carro. O carro terá alguns atributos, como modelo, ano e
# velocidade, e métodos para acelerar e imprimir as
# informações do carro.

class Carro:
    
    def __init__(self,modelo,ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
        
    def aceleracao(self, kilometros):
        self.velocidade += kilometros
        print (" O carro acelerou", self.velocidade,"kilometros")
        
        
    def diminuir(self, kilometros):
        self.velocidade -= kilometros
        print(" o carro diminuiu", self.velocidade, "kilometros")
        
    def sobre_o_carro(self):
        print("modelo: ",self.modelo)
        print("ano: ", self.ano)
        print("velocidade atual: ", self.velocidade,"kilometros por hora")
        
        
meu_carro = Carro("Commander", 2024)
meu_carro.aceleracao(50)
meu_carro.sobre_o_carro()
        
        
        
           