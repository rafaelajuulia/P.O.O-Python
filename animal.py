class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("O animal faz um som.")

    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late.")

# Criando objetos para testar as classes:
animal_generico = Animal(nome="Bicho", idade=3)
cachorro_rex = Cachorro(nome="Rex", idade=5)

# Chamando os métodos para ambos os objetos:
animal_generico.fazer_som()
animal_generico.imprimir_informacoes()

cachorro_rex.fazer_som()
cachorro_rex.imprimir_informacoes()
