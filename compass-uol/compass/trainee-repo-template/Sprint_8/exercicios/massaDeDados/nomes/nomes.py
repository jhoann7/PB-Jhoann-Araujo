import random
import time
import os
import names
import csv

random.seed(40)
nomes_unicos = 1000
nomes_aleatorios = 10000000

aux = []

for i in range(0, nomes_unicos):
    aux.append(names.get_full_name())
print(f"Gerando {nomes_aleatorios} nomes aleatórios.")

dados = []
for i in range(0, nomes_aleatorios):
    dados.append(random.choice(aux))

with open('nomes.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for nomes in dados:
        writer.writerow([nomes])