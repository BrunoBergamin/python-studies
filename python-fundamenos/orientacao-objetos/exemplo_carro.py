class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print(f"O carro {self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
        print(f"O carro {self.modelo} esta a {self.velocidade} km/h.")


carro1 = Carro("Ford", "Ka")
carro1.acelerar()
carro1.acelerar()
carro1.frear()
