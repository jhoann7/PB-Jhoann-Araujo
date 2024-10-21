class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"

    def __str__(self):
        return f"O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima} km/h, capacidade para {self.capacidade} passageiros e é da cor {self.cor}."

aviões = []
aviões.append(Aviao("BOIENG456", 1500, 400))
aviões.append(Aviao("Embraer Praetor 600", 863, 14))
aviões.append(Aviao("Antonov An-2", 258, 12))

for avião in aviões:
    print(avião)