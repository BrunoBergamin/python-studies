class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


conta1 = ContaBancaria("Bruno", 1000)
conta1.mostrar_saldo()
conta1.depositar(250)
conta1.sacar(100)
conta1.mostrar_saldo()
