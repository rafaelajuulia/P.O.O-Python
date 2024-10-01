class Carro:
    def __init__(self,marca, ano):
        self.marca = marca
        self.ano = ano
        
    def informacao(self):
        print(f"Marca do carro:{self.marca}")
        print(f"Ano do carro:{self.ano}")
        
carro = Carro("Jeep",2024)
carro.informacao()