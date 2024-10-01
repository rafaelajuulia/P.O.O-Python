

class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(self.nome, "não pode falar comendo")
            return
        
        if self.falando:
            print(self.nome, "Já está falando.")
            return
        
        print(self.nome,"Está falando.")
        self.falando = True

    def comer(self, alimento):
        if self.comendo:
            print(self.nome, "já esta comendo")
            return
        
        print(self.nome, "Esta comendo",alimento)
        self.comendo = True
    def para_comer(self):
        if not self.comendo:
           print(self.nome, "não esta comendo.") 
           return
        
        print(self.nome, "parou de comer.")
        self.comendo = False

p1 = Pessoa("Luíz", 29)
p1.comer("maçã")
p1.para_comer()
p1.comer("maçã")
