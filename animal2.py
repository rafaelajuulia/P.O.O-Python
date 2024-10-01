# Crie duas classes em Python: uma classe base chamada Animal e uma classe derivada chamada Cachorro. A
# classe Animal deve ter os seguintes atributos e métodos:

# Atributos:
# nome (string)
# idade (inteiro)

# Métodos:
# fazer_som(): Imprime uma mensagem genérica, como "O animal faz um som."
# imprimir_informacoes(): Imprime o nome e a idade do animal.

# A classe Cachorro deve herdar da classe Animal e adicionar o seguinte:
# Método:

# fazer_som(): Deve sobrescrever o método da classe Animal para imprimir "O cachorro late."
# Implemente as classes e escreva um programa que crie um objeto da classe Animal e outro da classe
# Cachorro, chamando o método fazer_som() e imprimir_informacoes() para ambos os objetos.

class Animal:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def fazer_som(self):
        print("O animal faz um som")
        
    def imprimir_informacoes(self):
        print("O nome do animal: ", self.nome)
        print("a idade do animal: ", self.idade)
        
class Cachorro(Animal):
    def fazer_som(self):
        print("o cachorro faz: au au")
    
        
        
animal = Animal("Animal generico",0)
cachorro = Cachorro("Nina",6)

animal.fazer_som()
animal.imprimir_informacoes()

cachorro.fazer_som()
cachorro.imprimir_informacoes()