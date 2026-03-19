class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Oi, meu nome e {self.nome} e tenho {self.idade} anos.")


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def estudar(self):
        print(f"{self.nome} esta estudando {self.curso}.")


aluno1 = Aluno("Bruno", 20, "Python")
aluno1.apresentar()
aluno1.estudar()
