class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f"Meu nome e {self.nome}, tenho {self.idade} anos e estudo {self.curso}.")

    def estudar(self, materia):
        print(f"{self.nome} esta estudando {materia}.")


aluno1 = Aluno("Bruno", 20, "Python")
aluno1.apresentar()
aluno1.estudar("orientacao a objetos")
