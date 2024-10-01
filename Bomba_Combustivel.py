# ▸Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# ▸Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# ▸tipoCombustivel.
# ▸valorLitro
# ▸quantidadeCombustivel
# ▸Possua no mínimo esses métodos:
# ▸abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada
# no veículo
# ▸abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo
# cliente.
# ▸alterarValor( ) – altera o valor do litro do combustível.
# ▸alterarCombustivel( ) – altera o tipo do combustível.
# ▸alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

# ▸OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.


class BombaCombustivel:
    
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        
    def abastecerPorValor(self,valor_abastecido):
        litros_abastecidos = valor_abastecido / self.quantidadeCombustivel
        self.quantidadeCombustivel -= litros_abastecidos
        return litros_abastecidos
    
    def abastecerPorLitro(self,litros_abastecidos):
        valor_pago = litros_abastecidos * self.valorLitro
        self.quantidadeCombustivel -= litros_abastecidos
        return valor_pago
    
    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor
        
    def alterarCombustivel(self,novo_tipo):
        self.tipoCombustivel = novo_tipo
        
    def alterarQuantidadeCombustivel(self,nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
        
bomba = BombaCombustivel("Gasolina", 5.0,1000)
print(bomba.abastecerPorValor(50))
print(bomba.abastecerPorLitro(20))
print(bomba.quantidadeCombustivel)
    
    