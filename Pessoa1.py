#Classe Pessoa: Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhecer, engordar, emagrecer, crescer.
#Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a
#idade dela menor que 21 anos, ela deve crescer 0,5 cm
#Pode possuir ou não parâmetros.


class Pessoa:
    
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
     
       
        
    def crescer(self, ano):
        if self.idade < 21:
            self.altura += 0.005 * ano
            
        else:
            print("Altura maxima alcançada")
            
    def envelhecer(self,anos):
        self.idade += anos
            
    def engordar(self,kilos):
        self.peso += kilos
        
    def emagrecer(self,kilos):
        self.peso -= kilos
        
    def informacao(self):
        print("o nome da pessoa é: ", self.nome)
        print("A idade da pessoa é:",self.idade)
        print(" Seu peso atual: ", self.peso)
        print("A altura da pessoa é: ", self.altura)
        
        
pessoa = Pessoa("Raju",19,79.9,1.64)
pessoa.envelhecer(4)
pessoa.emagrecer(20.0)
pessoa.informacao()
