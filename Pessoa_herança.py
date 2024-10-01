# Crie um programa que define uma classe pessoa, com nome, idade
# e data de nascimento.
# Ainda neste programa crie uma outra classe, aluno, que herde a
# classe pessoa, e além disso tenha um atributo matrícula. Na
# execução do programa o usuário deve preencher todas as
# informações de um funcionário.

class Pessoa:
    def __init__(self, nome, idade, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento

# Agora, criaremos a classe Aluno, que herda da classe Pessoa e adiciona o atributo matrícula:

class Aluno(Pessoa):
    def __init__(self, nome, idade, data_nascimento, matricula):
        super().__init__(nome, idade, data_nascimento)
        self.matricula = matricula

# Vamos pedir ao usuário para preencher as informações:

def main():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    data_nascimento = input("Digite a data de nascimento do aluno (no formato dd/mm/aaaa): ")
    matricula = input("Digite a matrícula do aluno: ")

    aluno = Aluno(nome, idade, data_nascimento, matricula)

    # Exibindo as informações do aluno:
    print("\nInformações do Aluno:")
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Data de Nascimento: {aluno.data_nascimento}")
    print(f"Matrícula: {aluno.matricula}")

if __name__ == "__main__":
    main()
